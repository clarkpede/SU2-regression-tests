SU2 Regression Tests
===================

These regression tests are intended to benchmark SU2 behavior at various
commits.  The current continuous integration system only checks the
transient behavior.  Because of this, non-trivial changes to the
numerics can cause the CI tests to fail.  Nevertheless, changes to the
transient solution do not always produce significant changes in the
converged solution. These tests allow a closer look. Both the
convergence history and the converged solution are compared for a few
simple cases.

Note that these tests are not intended to be a proper verification or
validation of the SU2 code.  They are intended to show how the
convergence and converged solution differ between two versions of SU2,
as a quick check.
