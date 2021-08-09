# Copyright 2020 The TensorFlow Probability Authors. All Rights Reserved.
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# THIS FILE IS AUTO-GENERATED BY `gen_linear_operators.py`.
# DO NOT MODIFY DIRECTLY.
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# pylint: disable=g-import-not-at-top
# pylint: disable=g-direct-tensorflow-import
# pylint: disable=g-bad-import-order
# pylint: disable=unused-import
# pylint: disable=line-too-long
# pylint: disable=reimported
# pylint: disable=g-bool-id-comparison
# pylint: disable=g-statement-before-imports
# pylint: disable=bad-continuation
# pylint: disable=useless-import-alias
# pylint: disable=property-with-parameters
# pylint: disable=trailing-whitespace

# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Registrations for LinearOperator.adjoint."""

from __future__ import absolute_import
from __future__ import division
# [internal] enable type annotations
from __future__ import print_function

from tensorflow_probability.python.internal.backend.jax import numpy_math as math_ops
from tensorflow_probability.python.internal.backend.jax.gen import linear_operator
from tensorflow_probability.python.internal.backend.jax.gen import linear_operator_adjoint
from tensorflow_probability.python.internal.backend.jax.gen import linear_operator_algebra
from tensorflow_probability.python.internal.backend.jax.gen import linear_operator_block_diag
from tensorflow_probability.python.internal.backend.jax.gen import linear_operator_circulant
from tensorflow_probability.python.internal.backend.jax.gen import linear_operator_diag
from tensorflow_probability.python.internal.backend.jax.gen import linear_operator_householder
from tensorflow_probability.python.internal.backend.jax.gen import linear_operator_identity
from tensorflow_probability.python.internal.backend.jax.gen import linear_operator_kronecker


# By default, return LinearOperatorAdjoint which switched the .matmul
# and .solve methods.
@linear_operator_algebra.RegisterAdjoint(linear_operator.LinearOperator)
def _adjoint_linear_operator(linop):
  return linear_operator_adjoint.LinearOperatorAdjoint(
      linop,
      is_non_singular=linop.is_non_singular,
      is_self_adjoint=linop.is_self_adjoint,
      is_positive_definite=linop.is_positive_definite,
      is_square=linop.is_square)


@linear_operator_algebra.RegisterAdjoint(
    linear_operator_adjoint.LinearOperatorAdjoint)
def _adjoint_adjoint_linear_operator(linop):
  return linop.operator


@linear_operator_algebra.RegisterAdjoint(
    linear_operator_identity.LinearOperatorIdentity)
def _adjoint_identity(identity_operator):
  return identity_operator


@linear_operator_algebra.RegisterAdjoint(
    linear_operator_identity.LinearOperatorScaledIdentity)
def _adjoint_scaled_identity(identity_operator):
  multiplier = identity_operator.multiplier
  if np.issubdtype(multiplier.dtype, np.complexfloating):
    multiplier = math_ops.conj(multiplier)

  return linear_operator_identity.LinearOperatorScaledIdentity(
      num_rows=identity_operator._num_rows,  # pylint: disable=protected-access
      multiplier=multiplier,
      is_non_singular=identity_operator.is_non_singular,
      is_self_adjoint=identity_operator.is_self_adjoint,
      is_positive_definite=identity_operator.is_positive_definite,
      is_square=True)


@linear_operator_algebra.RegisterAdjoint(
    linear_operator_diag.LinearOperatorDiag)
def _adjoint_diag(diag_operator):
  diag = diag_operator.diag
  if np.issubdtype(diag.dtype, np.complexfloating):
    diag = math_ops.conj(diag)

  return linear_operator_diag.LinearOperatorDiag(
      diag=diag,
      is_non_singular=diag_operator.is_non_singular,
      is_self_adjoint=diag_operator.is_self_adjoint,
      is_positive_definite=diag_operator.is_positive_definite,
      is_square=True)


@linear_operator_algebra.RegisterAdjoint(
    linear_operator_block_diag.LinearOperatorBlockDiag)
def _adjoint_block_diag(block_diag_operator):
    # We take the adjoint of each block on the diagonal.
  return linear_operator_block_diag.LinearOperatorBlockDiag(
      operators=[
          operator.adjoint() for operator in block_diag_operator.operators],
      is_non_singular=block_diag_operator.is_non_singular,
      is_self_adjoint=block_diag_operator.is_self_adjoint,
      is_positive_definite=block_diag_operator.is_positive_definite,
      is_square=True)


@linear_operator_algebra.RegisterAdjoint(
    linear_operator_kronecker.LinearOperatorKronecker)
def _adjoint_kronecker(kronecker_operator):
    # Adjoint of a Kronecker product is the Kronecker product
    # of adjoints.
  return linear_operator_kronecker.LinearOperatorKronecker(
      operators=[
          operator.adjoint() for operator in kronecker_operator.operators],
      is_non_singular=kronecker_operator.is_non_singular,
      is_self_adjoint=kronecker_operator.is_self_adjoint,
      is_positive_definite=kronecker_operator.is_positive_definite,
      is_square=True)


@linear_operator_algebra.RegisterAdjoint(
    linear_operator_circulant.LinearOperatorCirculant)
def _adjoint_circulant(circulant_operator):
  spectrum = circulant_operator.spectrum
  if np.issubdtype(spectrum.dtype, np.complexfloating):
    spectrum = math_ops.conj(spectrum)

  # Conjugating the spectrum is sufficient to get the adjoint.
  return linear_operator_circulant.LinearOperatorCirculant(
      spectrum=spectrum,
      is_non_singular=circulant_operator.is_non_singular,
      is_self_adjoint=circulant_operator.is_self_adjoint,
      is_positive_definite=circulant_operator.is_positive_definite,
      is_square=True)


@linear_operator_algebra.RegisterAdjoint(
    linear_operator_householder.LinearOperatorHouseholder)
def _adjoint_householder(householder_operator):
  return householder_operator

import numpy as np; onp = np
from tensorflow_probability.python.internal.backend.jax import linalg_impl as _linalg
from tensorflow_probability.python.internal.backend.jax import ops as _ops
from tensorflow_probability.python.internal.backend.jax.gen import tensor_shape

from tensorflow_probability.python.internal.backend.jax import private
distribution_util = private.LazyLoader(
    "distribution_util", globals(),
    "tensorflow_probability.substrates.numpy.internal.distribution_util")
tensorshape_util = private.LazyLoader(
    "tensorshape_util", globals(),
    "tensorflow_probability.substrates.numpy.internal.tensorshape_util")

