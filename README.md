# CARP IPDM-GO REPORT

![CACHET](cachet.png)

##
The Copenhagen Center for Health Technology (CACHET) Research Platform (CARP) enables researchers to run mobile health (mHealth) studies where data is collected on participant's smartphones and wearable devices. Data is securely uploaded and managed in a hosting infrastructure managed by the Technical University of Denmark.

CARP is a platform for running research studies in the health domain – also known as Digital Phenotyping. Such studies range from technical feasibility studies of novel technology to large-scale clinical studies. The platform is very versatile both in terms of support for different types of health domains, as well as in terms of technical support and configuration.

Environments 
-----------------

> Changing the **[CARP]** environment: 
>  - replace the environment in the following directory: `carp_fastapi.api.services`
>  - *env.BASE_URL["production"]; env.BASE_URL["staging"]; env.BASE_URL["development"]; env.BASE_URL["test"]; env.BASE_URL["local"]..*


Install requirements
-----------------

**Provision for Production:** 
 >  - ~`cd` into `carp.client-fastapi` directory and use the bash-command: 
 > - bash deployment.sh production up
 > - Done :)


**Run locally:**
>  - ~`cd` into `carp.client-fastapi` directory and use the command: 
>  - uvicorn run:app --reload
>  - Done :)

Dependencies
-----------------
- [CARP CLIENT API ASYNC](https://pypi.org/project/carp-async-api)
         
References
-----------------
- Copenhagen Center for Health Technology [CACHET](https://cachet.dk)
- [CARP Webpage](https://carp.cachet.dk).
- [CANS Management Dashboard](https://cans.cachet.dk).
- [CARP Core](https://carp.cachet.dk/core/)

