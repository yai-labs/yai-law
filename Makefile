# ===============================
# yai-law — Quality Gates (hard mode)
# ===============================

SHELL := /bin/bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c

DOXYGEN ?= doxygen
DOXY_OUT ?= dist/docs

.PHONY: \
	all ci check \
	lint-layout lint-json lint-docs lint-legacy-paths \
	formal-coverage formal-bindings-check \
	validate-law-registry \
	docs docs-clean clean tree

all: check

ci: \
	lint-layout \
	lint-json \
	lint-legacy-paths \
	check \
	formal-bindings-check \
	formal-coverage \
	validate-law-registry \
	lint-docs

# --------------------------------
# Hard-mode layout gate
# --------------------------------
lint-layout:
	@echo "[layout] enforcing canonical repository roots..."
	@test -d authority
	@test -d foundation
	@test -d runtime
	@test -d contracts
	@test -d registry
	@test -d schema
	@test -d packs
	@test -d formal
	@test -d tools
	@test -d vectors
	@test ! -d law
	@test ! -d specs
	@test ! -d compliance
	@echo "[layout] OK"

# --------------------------------
# Basic checks (presence + JSON parse)
# --------------------------------
check: lint-layout lint-json lint-legacy-paths
	@echo "[check] checking canonical surface files..."
	@test -f contracts/protocol/include/yai_protocol_ids.h
	@test -f contracts/vault/include/yai_vault_abi.h
	@test -f contracts/protocol/runtime/include/rpc_runtime.h
	@test -f registry/primitives.v1.json
	@test -f registry/commands.v1.json
	@test -f registry/artifacts.v1.json
	@test -f schema/bundle_manifest.v1.schema.json
	@test -f schema/evidence_index.v1.schema.json
	@test -f packs/compliance/gdpr-eu/2026Q1/pack.meta.json
	@echo "[check] OK"

lint-json:
	@echo "[json] validating all *.json parse..."
	@command -v python3 >/dev/null 2>&1 || { echo "[json] python3 not found"; exit 1; }
	@failed=0; \
	while IFS= read -r -d '' f; do \
		if ! python3 -m json.tool "$$f" >/dev/null 2>&1; then \
			echo "[json] invalid: $$f"; \
			failed=1; \
		fi; \
	done < <(find . \
		-path './.git' -prune -o \
		-path './dist' -prune -o \
		-path './build' -prune -o \
		-path './target' -prune -o \
		-type f -name '*.json' -print0); \
	test $$failed -eq 0
	@echo "[json] OK"

lint-legacy-paths:
	@echo "[paths] rejecting legacy path references..."
	@! rg -n '(^|[[:space:]`"(])law/(normative|surfaces|bindings|abi|packs)|docs/spec_map\.pointer\.md' . \
		--glob '!dist/**' \
		--glob '!.git/**'
	@echo "[paths] OK"

lint-docs:
	@echo "[docs] checking links..."
	@bash tools/validate/check_links.sh
	@echo "[docs] OK"

# --------------------------------
# Formal gates
# --------------------------------
formal-bindings-check:
	@echo "[formal] checking required bindings..."
	@test -f contracts/protocol/BINDING.md
	@test -f contracts/vault/BINDING.md
	@test -f contracts/control/BINDING.md
	@test -f contracts/cli/BINDING.md
	@test -f contracts/compliance/README.md
	@test -f runtime/kernel/BINDING.md
	@test -f runtime/mind/graph/BINDING.md
	@echo "[formal] bindings: OK"

formal-coverage:
	@echo "[formal] validating traceability coverage..."
	@python3 tools/formal/validate_traceability.py
	@echo "[formal] coverage: OK"

validate-law-registry:
	@echo "[registry] validating canonical registries..."
	@python3 tools/validate/validate_registry.py
	@echo "[registry] OK"

# --------------------------------
# Docs (Doxygen)
# --------------------------------
docs:
	@echo "[doxygen] generating docs..."
	@mkdir -p $(DOXY_OUT)
	@$(DOXYGEN) Doxyfile
	@echo "[doxygen] OK: $(DOXY_OUT)/doxygen/html/index.html"

docs-clean:
	@rm -rf $(DOXY_OUT)

clean: docs-clean

tree:
	@find . \
		-path './.git' -prune -o \
		-path './dist' -prune -o \
		-path './build' -prune -o \
		-path './target' -prune -o \
		-type f -print | sort
