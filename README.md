# Workflow Process and Modelling 
This is a repository of code used for the Workflow Modelling Assignment practicals for Integrated Geospatial Workflows, Geoinformatics, ITC Faculty, May 28th 2019.

## Description
A workflow is the automation of a process, in whole or part, where tasks are assigned and documents and data are passed from one participant to another for action, according to a set of procedural rules. This repository contains code implementation for creating Web Processing Services, Utilizing 3rd Party WPS's and implementing a Geoprocessing Workflow (GPW) using the process chaining concept and using a Workflow Management System.(WfMS).

## Assignment 1: WPS
The OGC Web Processing Service offers a standardized interface for publishing of geospatial processes, algorithms, and calculations. It offers three key operations for interacting with remote processes which are mainly the GetCapabilities, DescribeProcess and the Execute.

**Task** : Implement a Geoprocessing Function as a WPS. Here I implemented envelope function to retrieve the coordinates of the bounding box of a feature.
View the code implementation [here](https://github.com/SophiaNM/workflows_assignment/tree/master/assign1_wps)

## Assignment 2: Process Chaining
The OGC process chaining is a concept where two or more WPS are combined into a single powerful WPS.

**Task** : Produce a statistics which shows the length of streets within a radius of 1000m from the center of every neighbourhood using OGC Web Processing Service and Process Chaining. 
This is executed using the following WPS functions available in the wpsserver:
* gs:Centroid
* gs:BufferFeatureCollection
* gs:IntersectionFeatureCollection
* gs:Length

View the code implementation [here](https://github.com/SophiaNM/workflows_assignment/tree/master/assign2_processchain)


## Assignment 3: Workflow Modelling
A workflow management system defines, manages and executes workflows through software whose order of execution is driven by a computer representation of the workflow logic.  

**Task** :  Produce a statistics which shows the length of streets within a radius of 1000m from the center of every neighbourhood using WorkflowApp.
WorkflowApp is used to compose a workflow using WPS functions that are similar to the process chain implementation.This is then submitted to a workflow engine which executes the process chain to give results that are visualized in the workflow client.
View the workflow json and results [here](https://github.com/SophiaNM/workflows_assignment/tree/master/assign3_workflowmodel)

![](https://github.com/SophiaNM/workflows_assignment/blob/master/assign3_workflowmodel/process_chain_workflowmodel.JPG)*figure 1: WorkflowApp Implementation*


## Technologies Used
    - Python 3.7
    - Pycharm IDE
    - XML
    - WorkflowApp


### Contributions
Yet to complete loop functionality for process chaining. 
If you have ideas to make the code efficient you may contribute to this project.


## Known bugs
No known bugs so far. If found kindly create an issue.


## Contributors
    - Njeri Murage

### Contact Information
njerimurage92@gmail.com | n.murage@student.utwente.nl

Copyright © 2019. ITC Faculty, University of Twente. All rights reserved.