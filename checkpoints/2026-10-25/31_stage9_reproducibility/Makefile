# Stage 9 reproducibility entrypoint. Run from repo root:
# make -f checkpoints/2026-10-25/31_stage9_reproducibility/Makefile verify
PROJECT_ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/../../..)
STAGE9 := $(PROJECT_ROOT)/checkpoints/2026-10-25/31_stage9_reproducibility
LEAN_DIR := $(PROJECT_ROOT)/checkpoints/2026-10-24/18_lean_formal_proofs/lean
PAPER_DIR := $(PROJECT_ROOT)/checkpoints/2026-10-24/20_stage9_10_manuscript

.PHONY: deps verify formal pdf all

deps:
	python -m pip install -r "$(STAGE9)/requirements.txt"

verify:
	python "$(STAGE9)/verify_all.py"

formal:
	cd "$(LEAN_DIR)" && lake update && lake build

pdf:
	cd "$(PAPER_DIR)" && latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error paper.tex

all: verify formal pdf
