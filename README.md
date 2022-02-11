# TIF-Metabolite-Analysis
Data processing for LC-Mass Spectrometry developed for Matthew Vander Heiden Lab at The Koch Institute for Integrative Cancer Research at MIT

Labs often run LC-MS to quantify the metabolites in Fetal Bovine Serum for tissue culture. The LC-MS data produced is structure, but even with excel macros, the data processing can take over 20 hours. This data processing includes building concentration regressions based either on internal or external standards. With input from the user, this software compiles data from excel files exported to quantify various measurements for each metabolite. This can be used as input to many metabolite analysis programs. 

In the Vander Heiden Lab, many scientists intuitively pick ranges in the regression to exclude anomalous data to improve accuracy. Additionally, they favor information that best models typical cellular levels of metabolites. I modeled such logic within the program and achieved similar preformace to a scientist compiling the data. 
</br>
</br>
Below is a snapshot of an example of the input excel file: 
<img width="1395" alt="Metabolite Excel Snapshot" src="https://user-images.githubusercontent.com/85134229/153636326-c268ede0-560a-48a0-8c0e-5bd67d07ef76.png">
</br>
</br>
</br>
And an example output excel file: 
<img width="1187" alt="Results Excel Snapshot" src="https://user-images.githubusercontent.com/85134229/153638849-3d497ca3-8062-4f0d-9ffe-86fa1c4e0fab.png">
