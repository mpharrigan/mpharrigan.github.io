---
layout: page
title: Research
image: kchan.png
---


## Ion channels

Sodium channels initiate signaling in neurons and other cells which go
on to become sensations of pleasure and pain, as well as thoughts and
feelings.  In a collaboration with the [duBois] lab and with the help
of [Folding@Home], we are launching a large scale molecular dynamics
study of the voltage gated sodium channel.

We're studying the dynamics of transitions between the open and closed
states mediated by the voltage sensing domains. Our experimental
collaborators will probe sodium channel function through the use of
natural toxins secreted by frogs in the Amazon rainforest.  By
combining theory and experiment, we can propose and test derivatives
of these toxins which have positive therapeutic effects.


[dubois]: http://duboislab.stanford.edu/
[folding@home]: https://folding.stanford.edu/

## Markov Modelling

Our lab develops and applies novel statistical techniques to
understand and interpret the huge volume of data returned from a
molecular dynamics study. Particularly, we use Markov State Models
(MSMs) which model conformational dynamics as a series of memoryless
jumps between microstates. 

### Solvent dynamics

I've introduced a new method for including solvent degrees of freedom
in MSM analysis. Check out the [paper][shellspaper] introducing
the method and the [code][shellsgithub]. We're working on applying it
to new and exciting systems.

[shellspaper]: http://dx.doi.org/10.1021/ct5010017
[shellsgithub]: https://github.com/mpharrigan/wetmsm

### Adaptive sampling

MSMs offer a convenient framework for analyzing the results of
simulations, but they can also be used to direct simulation. In an
adaptive sampling scheme, uncertainty in particular MSM state
transition probabilities are used to seed new simulations to speed
convergence of the model.

## Papers

{% include_relative citations.html %}


<!-- vim: tw=70
-->
