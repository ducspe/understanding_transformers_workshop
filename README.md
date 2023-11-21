# Understanding Transformers Workshop
Hello! Thank you for your interest in our transformer workshop!

In this workshop I will act as a synthesizer of various online resources and material provided by the broader AI community.

The prerequisites for this workshop are the ability to read Python and know the basics in Calculus, Probability and Statistics. It is helpful if you are acquainted with PyTorch and Neural Networks, but these latter aspects are not a must.

During the first day we will focus on theory and applications of transformers. For this we will use slides and whiteboards. I will reference all the articles and resources from which useful material was taken at the bottom of each slide. This way you can read the articles behind each slide and get a broader understanding in your own spare time after the workshop.

The second day will be a practical session, where we will investigate the code pre-written in a jupyter notebook. The jupyter notebook I generated using the resources from Andrej Karpathy, which I highly recommend. Please checkout https://github.com/karpathy/nanoGPT and https://github.com/karpathy/ng-video-lecture in particular if you want to review later some of the things we will discuss during the workshop.

We will go step-by-step through the slides and through the jupyter notebook code, explaining things at a deeper level, in order to get an intuitive understanding of how transformers are designed and how they work.

Since the audience is heterogeneous, with some participants knowing the prerequisites very well, and some less, the workshop will address this situation by making a parallel between the code, and Figure 1 (see **extra_material** folder) in the paper: "Attention is all you need" by Vaswani et al. This way, people who have better knowledge of Python, PyTorch, Calculus and Statistics will have the chance to understand and focus on the code details, whereas someone who is not as proficient in these things will still be able to follow along and have a bigger picture overview due to making parallels with the block diagram from the transformer paper. Thus, those participants who might lack some of the prerequisites, will abstract part of the details, but they will still gain an intuitive understanding about which components do what exactly, i.e. their functionality, how they are combined and how they interact.

Thank you for reading this, please continue with the environment setup instructions below, and see you in the Workshop!

Danu


### Environment Setup Instructions

Please install a Miniconda environment. You will find a Windows, macOS or Linux version here: https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html

Open a terminal and change directory to the git repository path: `cd cloned_repository_path`

We will now create a new conda environment with Python 3.8.10 as follows:

`conda create --name transformer_workshop python=3.8.10`

Type "yes" or "y" and press enter to install the required initialization dependencies.

We will activate the environment: 
`conda activate transformer_workshop`

And finally, we will install all the dependencies we need, in this case only pytorch:

`conda install -c pytorch pytorch==1.13.0`

Next, please install the Jupyter notebook: `pip install notebook`

Set up the newly created conda environment as a jupyter kernel:
- First install the necessary dependency: `pip install ipykernel`
- And then execute: 

`python -m ipykernel install --user --name transformer_workshop --display-name "TransformerWorkshop"`

Run the jupyter notebook start command in the terminal: `jupyter notebook` At this point your default browser should open a page where you will see the folder with all the git repository files, including **mini_gpt.ipynb**. Double click on it.

A page will open with the code for mini-gpt. Select the correct kernel name (i.e. "TransformerWorkshop") from the dropdown list on the right side of the page.

If everything was setup up correctly in the previous steps, you should be able to run the import statements in the first notebook cell and not get any dependency errors. Note that running a cell means we select the cell and click the triangle/"play" button, however your browser may offer other convenient keyboard shortcuts for this.

If imports are fine, run subsequently all the other cells to see if you don't get any runtime errors.

To terminate the jupyter notebook session press Ctrl+C and select "yes"/"y" option.

After the workshop, you can deactivate your conda environment via: `conda deactivate`

## Acknowledgments

Many thanks to the following institutions that made this work possible:

- German Climate Computing Center (DKRZ), Hamburg, Germany
- Helmholtz Center Hereon, Geesthacht, Germany
- Helmholtz AI

This work was supported by Helmholtz Association's Initiative and Networking Fund through Helmholtz AI [grant number: ZT-I-PF-5-01]. 
I also used resources of the Deutsches Klimarechenzentrum (DKRZ) granted by its Scientific Steering Committee (WLA) under project ID AIM.