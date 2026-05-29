"""Domain resolver entry point (invoked only after Boundary validation passes)."""

from __future__ import annotations

from typing import Any, Protocol

from src.entity.solver import TwoCellSolver


class DomainResolver(Protocol):
    """Resolves a validated puzzle matrix through the Domain pipeline."""

    def resolve(self, grid: list[list[int]]) -> Any:
        """Run Domain logic for a SIZE-validated matrix."""
        ...


class DomainResolverImpl:
    """Default Domain resolver wiring the FR-02~05 pipeline."""

    def __init__(self) -> None:
        """Create solver used after Boundary validation passes."""
        self._solver = TwoCellSolver()

    def resolve(self, grid: list[list[int]]) -> Any:
        """Run the two-cell solver for a validated puzzle matrix."""
        return self._solver.solve(grid)
