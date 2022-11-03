# Summary
### Sharing Pandas data frames as websites on AWS S3

<p> 
This project explores the link between CSV-files, Pandas data frames, HTML-files and AWS S3. The CSV-files are read into Pandas data frames and then converted into HTML-files and then uploaded on S3 as the 'ContentType': 'text/html'. This allows to create a simple website structure with an index HTML-file as a start page. The startpage links to the DF-subpages. This is an easy way to share data. The data can be public or private. In the latter case multiple ways to protect the data are available, which are not explored in detail here. 
</p> 

<p>
This project is based on the preliminary:<br>
<a href ="https://github.com/RolfChung/Boto3_FileManagement_on_AWS.git" target = _blank>
Boto3_FileManagement_on_AWS</a> project.
</p>


<p>
The project relies heavily on the  
<a href = https://boto3.amazonaws.com/v1/documentation/api/latest/index.html target=_blank> 
Boto3 documentation.</a> <br> 
According to the doc: 
</p> 

<p> 
“You use the AWS SDK for Python (Boto3) to create, configure, and manage AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service (Amazon S3). The SDK provides an object-oriented API as well as low-level access to AWS services.” 
</p> 

<p>This project creates an  

### S3_helpers_pckg 

<p> 
The package stores a class with useful helper functions, mostly manipulating the dicts of responses.<br> 
The functions are mostly self defined, but other functions for example from Github and the doc are integrated.<br> 
In this case credits are given.<br> 
The pckg is a work in progress. 

</p> 

<p>Several topics are examined here. <br> 
For example:</p> 
<ul> 
<li>Setting up AWS clients</li> 
<li>Pandas and HTML</li> 
<li>Converting Pandas data frames to HTML</li> 
<li>Styling a data frame</li> 
<li>Pandas data frames and csv downloads from S3</li> 
<li>Styling a data frame</li> Uploading HTML-files to AWS S3
<li>Creating an index html page</li> 
<li>Reading an streaming csv object into a Pandas data frame</li>     
<li>Uploading HTML-files to AWS S3</li>   
<li>Displaying an html file in a Jupyter notebook cell with</li> 
</ul> 

<p> 
The credentials are secured with a <a href="www.dotenv.org/docs" target=_blank> 
dotenv.</a>
</p> 
 