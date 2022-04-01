import jax
import matplotlib.pyplot as plt
import numpy as np
import jax.numpy as jnp

def f(x):
  return (x[0] - 1.0)**2 + (x[1] - 3.0)**2

x0 = np.zeros(2)
learning_rate = 0.01

ys = []
for step in range(1000):
  ys.append(f(x0))
  grad_f = jax.grad(f)(x0)
  x0 -= grad_f * learning_rate

plt.plot(ys)
print(f"Minimum: {x0}")


def tanh(x,y,z):  # Define a function
  y1 = jnp.exp(3*x**2-2*x*y+10*x*z**3)
  return (1.0 - y1) / (1.0 + y1)

grad_tanh = jax.grad(tanh)(x)  # Obtain its gradient function
print(grad_tanh(1.0))   # Evaluate it at x = 1.0
# prints 0.4199743
