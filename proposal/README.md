# Informatic Research Proposal - Docker-based high performance computing in the cloud

## Motivation

High Performance Computing (HPC) requires high performing infrastructures
like supercomputers or huge clusters of compute node to be run effectively.
This computational setup allows some complex computation,
usually a scientific computation simulation, to be done in a high
performing fashion that traditional consumer desktop computers cannot achieve.
However acquiring access to this computation resources are not easy, nor
cheap, i.e, you have to be member of a university, government
institute, licensed, or build your own cluster.

In scientific community, especially in scientific computation,
researchers utilize these infrastructures for their research. For
example, HemeLB that utilize Cray XT3 MPP TerraGrid Machine located on Pittsburgh,
and Cray XT4 at University of Edinburgh[1]. These infrastructures,
unfortunately often not available to most people or unfeasible to
replicate. Moreover, complex setup process and toolings needed further
discourage people from replicating computations from these researches.

Galaxy[2], a web-based reproducible research platform is developed to
answer to these issues. It allows its user to compose, customize, run
and share their simulations utilizing cloud computing resources.
However, these computational models are limited to the tools provided by
the web application, Galaxy, and the infrastructures that it rans on
(i.e, OS) which require researches/ computational researches to
understand/ have experience with the toolings provided or create their
own based on the restriction. For example, most of the tools that is ran
on Galaxy, require python script.

<!--Some research have tried to overcome this limitations by utilizing the-->
<!--power of cloud computing. Galaxy[2], for example tried to be-->
<!--the web-based reproducible research platform that-->
<!--allows everyon to compose, run, and share results of the research to-->
<!--everyone using the power of cloud computing. However, the degree of the-->
<!--computations configurations are limited to the resources that are available to the-->
<!--computing infrastructure and tools provided by Galaxy project.-->

Limitation above is the impetus for this project. In an ideal scenario,
researchers do not need to port their computation project to the provided toolings,
environment of an infrastructure of a computational models provider.
Researchers could just compose their computation project with whatever
tools and environment they are comfortable with and run with it. And
this is where docker[3] comes into the picture. Docker allows us to compose
our computation environment and tools as we wanted and allow it to be
shared easily. Our project will utilize this unique trait of docker to
allow researchers compose their computational project as they see fit.

There will be a web interface to set the running parameter of the computations
and to run the project utilizing cloud computing resources. This allows
researchers to be free from tools that they are not familiar with or
specific implementations which is a barrier for replication of project.
Infrastructure choice also become agnostic, our computational node do
not have to install dependencies or tools that each project needs
because it is already packaged in the containers, making the
computational node reusable with different projects without getting
bogged down with tools and variables of all projects.





## Background

In dealing with High Performance Computing, infrastructures are
typically required to be able to handle multi-core operations easily[4].
Be it parallel workload or distributed system workload. This has lead to
two separate computing paradigm we know as grid and cluster computing.

Cluster computing is a paradigm where two or more computing resources
are connected and used concurrently to run a single applications, often
the computing resources are made of highly homogenous or similar
computing unit mounted in a rack. The type of application run on cluster typically require highly parallel
computation like modelling and simulation. This type of application benefits
from having a highly interconnected node and data locality that clusters
provide[4].

On the other hand, Grid computing is a different beast altogether. It
allows heterogeneous computing resources, often geographically
distributed, to cooperate for a common goals. It is highly dynamic and
promis scaling infinitely without regards of physical location of the
computing resources[6]. In the UK, grid computing often utilized under
the banner of e-science[7], where they provide common middleware,
software, and services for scientists to collaborate on their project regardless of physical
locations.

Both of this type of HPC computing are traditionally done in an in-house
manner. Where Universities or government institutions set up a cluster of
computing resources or even a supercomputer to do HPC task. Grid
computations are also done on in house manner or even utilize public's
desktop computer for computational resources, example are the
folding@ home and genome@ home projects[8]. Currently however, computing
resources are available in the cheap. Cloud computing has entered into
the pictures and allow computing resources to be available with a
price tag attached to it. It is massively scalable, allow abstract
encapsulation of computing resources, dynamically configured,
delivered on-demand and driven by economies of scale[5].

Cloud computing allowed institutions to offload their pain in procuring
and maintaining computing resources to the vendors like Amazon, Google,
Microsoft and etc for a price. This price also been reduced multiple times [9][10][11]
that comes with economies of scale, making it financially less demanding to
run HPC applications without in-house resources. In fact, few HPC
applications has been run on the cloud, such as the nekkloud
project[12], NASA HPC Applications[13], and few other case study [14]
that shows that it is feasible to run HPC applications on the cloud,
albeit with performance overhead.

This development have make it possible for people or institutions with
enough financial means to do some heavy computations without having
access to this traditionally expensive in-house computing resources.

[need better transition from cloud computing HPC to the push for
reproducibility]
In scientific computing, there has been a push to make a computational
results reproducible even if it is complex[15]. This push make sures that
research results adhere to scientific method, that is reproducible by
our peers. As traditionally, HPC resources are in-house, this hinders
the reproducibility aspect of the research. However, with cloud, this
enable people to access this resources more easily, for example:
Galaxy[2] that enable people to compose, run, and share their
modelling simulation.





<!--* History of Research Computing-->
<!--* - Grid Computing-->
<!--* - Cloud Computing-->

<!--* Scientific Computing-->
<!--* - Reproducible research-->
<!--* - Science code manifesto-->
<!--* - Example of scientific computing-->



<!--This has been the condition for past decades [?] because access of-->
<!--computational power is hard to acquire back then [?]. Currently, with-->
<!--the introduction of new computational service such as Infrastructure as-->
<!--A Service, Hardware as a Service, cloud computing has allowed people to-->
<!--acquire this resources easily and dynamically.-->


## Methodology
Work in progress

## Main Claim
Work in progress

X is better than Y on task Z along some dimension W

Docker-based HPC computing in cloud is better than supercomputer on
scientific computing along some dimension of usability, openess,
replicability

**How to support this claim** Theoritical ? Experimental?


## Expected Outcome/ Success Criteria
Work in progress

Working prototype that enable docker based HPC computing to be done in the cloud,
that enable the computations to be done easily (usable), shared
(replicable), and inspected (openness).

On this project, the main example of the application to be used is
HemeLB.

## References

[1] Mazzeo, Marco D., and Peter V. Coveney. "HemeLB: A high performance parallel lattice-Boltzmann code for large scale fluid flow in complex geometries." Computer Physics Communications 178.12 (2008): 894-914.

[2] Goecks et al.: Galaxy: a comprehensive approach for supporting accessible, reproducible, and transparent computational research in the life sciences. Genome Biology 2010 11:R86.

[3] Docker - http://www.docker.com/

[4] Whitepaper: Intro to HPC on AWS - https://d0.awsstatic.com/whitepapers/Intro_to_HPC_on_AWS.pdf

[5] Cloud Computing and Grid Computing 360-Degree Compared  - I. Foster, Y. Zhao, I. Raicu and S. Lu, "Cloud Computing and Grid Computing 360-Degree Compared," Grid Computing Environments Workshop, 2008. GCE '08, Austin, TX, 2008, pp. 1-10.  doi: 10.1109/GCE.2008.4738445

[6] Berman, Fran, Geoffrey Fox, and Anthony JG Hey. Grid computing: making the global infrastructure a reality. Vol. 2. John Wiley and sons, 2003.

[7] Hey, Tony, and Anne E. Trefethen. "Cyberinfrastructure for e-Science." Science 308.5723 (2005): 817-821.

[8] Larson, Stefan M., et al. "Folding@ Home and Genome@ Home: Using distributed computing to tackle previously intractable problems in computational biology." arXiv preprint arXiv:0901.0866 (2009).

[9] https://aws.amazon.com/blogs/aws/aws-price-reduction-42-ec2-s3-rds-elasticache-and-elastic-mapreduce/

[10] https://azure.microsoft.com/en-us/blog/storage-price-match/

[11] http://techcrunch.com/2014/03/25/google-drops-prices-for-compute-and-app-engine-by-over-30-cloud-storage-by-68-introduces-sustained-use-discounts/

[12] Cohen, Johanne, et al. "Nekkloud: A software environment for high-order finite element analysis on clusters and clouds." Cluster Computing (CLUSTER), 2013 IEEE International Conference on. IEEE, 2013.

[13] Mehrotra, Piyush, et al. "Performance evaluation of Amazon EC2 for NASA HPC applications." Proceedings of the 3rd workshop on Scientific Cloud Computing Date. ACM, 2012.

[14] He, Qiming, et al. "Case study for running HPC applications in public clouds." Proceedings of the 19th ACM International Symposium on High Performance Distributed Computing. ACM, 2010.

[15] Marwick, Ben. "Computational Reproducibility in Archaeological Research: Basic Principles and a Case Study of Their Implementation." Journal of Archaeological Method and Theory (2016): 1-27.