from manimlib.imports import *
from my_project.qubit import *

OUTPUT_DIRECTORY = "qubit"


# 
# hadamard rotation
# 

class BlochSphereHadamardRotate_once_with_sphere_fast(BlochSphereHadamardRotate):
	CONFIG = {
		"rotate_sphere": True,
		"rotate_time": 5,
		"rotate_amount": 1,
	}
class BlochSphereHadamardRotate_once_with_sphere_slow(BlochSphereHadamardRotate):
	CONFIG = {
		"rotate_sphere": True,
		"rotate_time": 8,
		"rotate_amount": 1,
	}
class BlochSphereHadamardRotate_once_without_sphere_fast(BlochSphereHadamardRotate):
	CONFIG = {
		"rotate_sphere": False,
		"rotate_time": 5,
		"rotate_amount": 1,
	}
class BlochSphereHadamardRotate_once_without_sphere_slow(BlochSphereHadamardRotate):
	CONFIG = {
		"rotate_sphere": False,
		"rotate_time": 8,
		"rotate_amount": 1,
	}
class BlochSphereHadamardRotate_twice_with_sphere_fast(BlochSphereHadamardRotate):
	CONFIG = {
		"rotate_sphere": True,
		"rotate_time": 5,
		"rotate_amount": 2,
	}
class BlochSphereHadamardRotate_twice_with_sphere_slow(BlochSphereHadamardRotate):
	CONFIG = {
		"rotate_sphere": True,
		"rotate_time": 8,
		"rotate_amount": 2,
	}
class BlochSphereHadamardRotate_twice_without_sphere_fast(BlochSphereHadamardRotate):
	CONFIG = {
		"rotate_sphere": False,
		"rotate_time": 5,
		"rotate_amount": 2,
	}
class BlochSphereHadamardRotate_twice_without_sphere_slow(BlochSphereHadamardRotate):
	CONFIG = {
		"rotate_sphere": False,
		"rotate_time": 8,
		"rotate_amount": 2,
	}


# 
# regular examples
# 
class BlochSphere_example_X(BlochSphere):
	CONFIG = {
		"operators": [
			Pauli_x,
		],
		"operator_names": [
			"Pauli X",
		],
	}
class BlochSphere_example_Y(BlochSphere):
	CONFIG = {
		"operators": [
			Pauli_y,
		],
		"operator_names": [
			"Pauli Y",
		],
	}
class BlochSphere_example_Z(BlochSphere):
	CONFIG = {
		"operators": [
			Pauli_z,
		],
		"operator_names": [
			"Pauli Z",
		],
	}

class BlochSphere_example_X_X(BlochSphere):
	CONFIG = {
		"operators": [
			Pauli_x,
			Pauli_x,
		],
		"operator_names": [
			"Pauli X",
			"Pauli X",
		],
	}
class BlochSphere_example_Y_Y(BlochSphere):
	CONFIG = {
		"operators": [
			Pauli_y,
			Pauli_y,
		],
		"operator_names": [
			"Pauli Y",
			"Pauli Y",
		],
	}
class BlochSphere_example_Z_Z(BlochSphere):
	CONFIG = {
		"operators": [
			Pauli_z,
			Pauli_z,
		],
		"operator_names": [
			"Pauli Z",
			"Pauli Z",
		],
	}

class BlochSphere_example_H_H(BlochSphere):
	CONFIG = {
		"operators": [
			Hadamard,
			Hadamard,
		],
		"operator_names": [
			"Hadamard",
			"Hadamard",
		],
	}
class BlochSphere_example_H_Z(BlochSphere):
	CONFIG = {
		"operators": [
			Hadamard,
			Pauli_z,
		],
		"operator_names": [
			"Hadamard",
			"Pauli Z",
		],
	}
class BlochSphere_example_H_Z_H(BlochSphere):
	CONFIG = {
		"operators": [
			Hadamard,
			Pauli_z,
			Hadamard,
		],
		"operator_names": [
			"Hadamard",
			"Pauli Z",
			"Hadamard",
		],
	}
class BlochSphere_example_H_X_H(BlochSphere):
	CONFIG = {
		"operators": [
			Hadamard,
			Pauli_x,
			Hadamard,
		],
		"operator_names": [
			"Hadamard",
			"Pauli X",
			"Hadamard",
		],
	}

class BlochSphere_example_SX_SX(BlochSphere):
	CONFIG = {
		"operators": [
			Sqrt_x,
			Sqrt_x,
		],
		"operator_names": [
			"Sqrt of X",
			"Sqrt of X",
		],
	}
class BlochSphere_example_SX_SX_SX_SX(BlochSphere):
	CONFIG = {
		"operators": [
			Sqrt_x,
			Sqrt_x,
			Sqrt_x,
			Sqrt_x,
		],
		"operator_names": [
			"Sqrt of X",
			"Sqrt of X",
			"Sqrt of X",
			"Sqrt of X",
		],
	}
class BlochSphere_example_SX_P90_SX(BlochSphere):
	CONFIG = {
		"operators": [
			Sqrt_x,
			Phase(90 * DEGREES),
			Sqrt_x,
		],
		"operator_names": [
			"Sqrt of X",
			"Phase 90",
			"Sqrt of X",
		],
	}
class BlochSphere_example_SX_P180_SX(BlochSphere):
	CONFIG = {
		"operators": [
			Sqrt_x,
			Phase(180 * DEGREES),
			Sqrt_x,
		],
		"operator_names": [
			"Sqrt of X",
			"Phase 180",
			"Sqrt of X",
		],
	}
class BlochSphere_example_SX_P270_SX(BlochSphere):
	CONFIG = {
		"operators": [
			Sqrt_x,
			Phase(270 * DEGREES),
			Sqrt_x,
		],
		"operator_names": [
			"Sqrt of X",
			"Phase 270",
			"Sqrt of X",
		],
	}
class BlochSphere_example_SX_P45_SX(BlochSphere):
	CONFIG = {
		"circle_xz_show": True,
		"operators": [
			Sqrt_x,
			Phase(45 * DEGREES),
			Sqrt_x,
		],
		"operator_names": [
			"Sqrt of X",
			"Phase 45",
			"Sqrt of X",
		],
	}
class BlochSphere_example_SX_P45_SX_SX(BlochSphere):
	CONFIG = {
		"circle_xz_show": True,
		"operators": [
			Sqrt_x,
			Phase(45 * DEGREES),
			Sqrt_x,
			Sqrt_x,
		],
		"operator_names": [
			"Sqrt of X",
			"Phase 45",
			"Sqrt of X",
			"Sqrt of X",
		],
	}
class BlochSphere_example_SX_P45_SX_SX_SX_SX(BlochSphere):
	CONFIG = {
		"circle_xz_show": True,
		"operators": [
			Sqrt_x,
			Phase(45 * DEGREES),
			Sqrt_x,
			Sqrt_x,
			Sqrt_x,
			Sqrt_x,
		],
		"operator_names": [
			"Sqrt of X",
			"Phase 45",
			"Sqrt of X",
			"Sqrt of X",
			"Sqrt of X",
			"Sqrt of X",
		],
	}
class BlochSphere_example_SX_P45_SX_Y_SX(BlochSphere):
	CONFIG = {
		"circle_xz_show": True,
		"operators": [
			Sqrt_x,
			Phase(45 * DEGREES),
			Sqrt_x,
			Pauli_y,
			Sqrt_x,
		],
		"operator_names": [
			"Sqrt of X",
			"Phase 45",
			"Sqrt of X",
			"Pauli Y",
			"Sqrt of X",
		],
	}

class BlochSphere_example_H_P180(BlochSphere):
	CONFIG = {
		"operators": [
			Hadamard,
			Phase(180 * DEGREES),
		],
		"operator_names": [
			"Hadamard",
			"Phase 180",
		],
	}
class BlochSphere_example_P180_H(BlochSphere):
	CONFIG = {
		"operators": [
			Phase(180 * DEGREES),
			Hadamard,
		],
		"operator_names": [
			"Phase 180",
			"Hadamard",
		],
	}
class BlochSphere_example_H_P180_H(BlochSphere):
	CONFIG = {
		"operators": [
			Hadamard,
			Phase(180 * DEGREES),
			Hadamard,
		],
		"operator_names": [
			"Hadamard",
			"Phase 180",
			"Hadamard",
		],
	}
class BlochSphere_example_H_P90(BlochSphere):
	CONFIG = {
		"operators": [
			Hadamard,
			Phase(90 * DEGREES),
		],
		"operator_names": [
			"Hadamard",
			"Phase 90",
		],
	}
class BlochSphere_example_H_P90_H(BlochSphere):
	CONFIG = {
		"operators": [
			Hadamard,
			Phase(90 * DEGREES),
			Hadamard,
		],
		"operator_names": [
			"Hadamard",
			"Phase 90",
			"Hadamard",
		],
	}
class BlochSphere_example_H_P90_H_SX(BlochSphere):
	CONFIG = {
		"operators": [
			Hadamard,
			Phase(90 * DEGREES),
			Hadamard,
			Sqrt_x,
		],
		"operator_names": [
			"Hadamard",
			"Phase 90",
			"Hadamard",
			"Sqrt of X",
		],
	}
class BlochSphere_example_H_P90_H_H(BlochSphere):
	CONFIG = {
		"operators": [
			Hadamard,
			Phase(90 * DEGREES),
			Hadamard,
			Hadamard,
		],
		"operator_names": [
			"Hadamard",
			"Phase 90",
			"Hadamard",
			"Hadamard",
		],
	}
class BlochSphere_example_H_P45_H(BlochSphere):
	CONFIG = {
		"operators": [
			Hadamard,
			Phase(45 * DEGREES),
			Hadamard,
		],
		"operator_names": [
			"Hadamard",
			"Phase 45",
			"Hadamard",
		],
	}


# 
# bloch sphere walk
# 

class BlochSphereWalk_example_1(BlochSphereWalk):
	def update_theta_and_phi(self):
		theta = 0
		phi   = 0

		# theta 0 -> 90
		for i in range(90):
			theta += 1*DEGREES
			self.update_state(theta, phi)
		self.wait(1)
		# phi 0 -> 90
		for i in range(90):
			phi += 1*DEGREES
			self.update_state(theta, phi)
		self.wait(1)
		# theta 90 -> 45
		for i in range(45):
			theta -= 1*DEGREES
			self.update_state(theta, phi)
		self.wait(1)
		# phi 90 -> 270
		for i in range(180):
			phi += 1*DEGREES
			self.update_state(theta, phi)
		self.wait(1)
		# theta 45 -> 135
		for i in range(90):
			theta += 1*DEGREES
			self.update_state(theta, phi)
		self.wait(1)
		# phi 270 -> 0
		for i in range(90):
			phi += 1*DEGREES
			self.update_state(theta, phi)
		self.wait(1)
		# theta 135 -> 0
		for i in range(135):
			theta -= 1*DEGREES
			self.update_state(theta, phi)
		self.wait(1)

class BlochSphereWalk_example_2(BlochSphereWalk):
	def update_theta_and_phi(self):
		theta = 0
		phi   = 0

		# theta   0 ->  90
		for i in range(90):
			theta += 1*DEGREES
			self.update_state(theta, phi)
		self.wait(1)
		# theta  90 -> 180
		for i in range(90):
			theta += 1*DEGREES
			self.update_state(theta, phi)
		self.wait(1)
		# phi jump from 0 to 180
		phi = 180
		# theta 180 ->  90
		for i in range(90):
			theta -= 1*DEGREES
			self.update_state(theta, phi)
		self.wait(1)
		# theta  90 ->   0
		for i in range(90):
			theta -= 1*DEGREES
			self.update_state(theta, phi)
		self.wait(1)

