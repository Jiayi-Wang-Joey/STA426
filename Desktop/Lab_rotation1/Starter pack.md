## Starter pack
### Misc
- [ ] Join our Slack community.
- [ ] Post there your availability for the first meeting :)
- [ ] Let us know what your GitHub account is, so we can add you to the project. The request may take up to a day or two to be processed by the admin, so don't worry yet about tasks related to cloning and inspecting the repository.
- [ ] Make sure you can [access the Euler cluster](https://scicomp.ethz.ch/wiki/Getting_started_with_clusters#Euler). For example, try to log in and run simplest commands, as `pwd`.

### Introduction to inverse RL
The purpose of these tasks is to help you acquire expertise in inverse reinforcement learning. There are multiple paths towards this goal, so if you find a better lecture/book chapter/article, feel free to go for it.
I personally find P.N. Edwards' article [How to read a book](https://pne.people.si.umich.edu/PDF/howtoread.pdf) useful. I also included some questions, so you can practice active learning. They are open-ended and hard, so don't treat this as an assignment – if you can't answer any of them, we're here to provide some suggestions. But it'd be wonderful to brainstorm together, gathering different views on the topic! :)

- [ ] It's good to know the premise of the "ordinary" reinforcement learning. I recommend watching [the first lecture of David Silver's course](https://youtu.be/2pWv7GOvuf0?t=374).
- [ ] Before you proceed to inverse RL, let's put the learned material in some context. In our case we have a set of $n$ mutations $M=\{1, \dotsc, n\}$ and a _state_ is any subset of $M$.
	- Roughly, how many states do we have for $n$ possible mutations? What is it for $n=10$? And $n=30$?
	- What is the natural choice for the space of actions? How many of them do we have?
	- Can you propose a model of the transition probability $P(s_{k+1} \mid s_k, a)$?
	- How can we estimate the experts' policy $P(a \mid s)$?
- [ ] Now it's the time to move to inverse RL! It's the topic of Lecture 20 from Sergey Levine's course. On YouTube it's split into four videos: [Part 1](https://youtu.be/EcxpbhDeuZw), [Part 2](https://youtu.be/82Sr9YqeQNc), [Part 3](https://youtu.be/OsO2nLfxZVQ), [Part 4](https://youtu.be/ubwJh6jx4Dc).
	- How can we model possible _features_ for the reward design? How many of them will we have for $n$ mutations?
	- How can we evaluate the quality of the (learned) reward function?

### Getting started with the project
We think [Jax](https://jax.readthedocs.io/en/latest/notebooks/quickstart.html) will be easier to use in this project. If you however prefer PyTorch, feel free to go for it.

- [ ] To warm up with Jax: what is the gradient of the function $f(x, y, z) = 3x^2 - 2xy + 10xz^3$ evaluated at the point $(1, 2, 3)$?
- [ ] Read [Maximum Entropy Inverse Reinforcement Learning](https://www.aaai.org/Papers/AAAI/2008/AAAI08-227.pdf) by B.D. Ziebart et al. When reading, think about the following questions:
	- For how many mutations would this approach be feasible?
	- How can you use Jax to get the required gradient?
	- Having the gradient, how can you optimize the parameters to get the maximum likelihood estimate? (You can take a look at [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) or [Optax](https://github.com/deepmind/optax)).

### Repository
(After the GitHub access is granted).  
- [ ] Clone the [repository](https://github.com/cbg-ethz/PhIRL). If you need a brush up on Git, take a look at [Roger Dudler's Git Simple Guide](https://rogerdudler.github.io/git-guide/) (starting at the _checkout a repository_ section).
- [ ] Set up the repository as described in the ReadMe file. Run unit tests to see if everything is working.
- [ ] Take a brief look at the repository to see how it is structured. In particular, make sure you know how to answer the following questions:
	- What functionalities do we already have there?
	- How can I add an automated test?
	- Are there any bits unclear? (E.g., some documentation needs to be improved).
	- In case of any problems, do not hestitate to ask :)
