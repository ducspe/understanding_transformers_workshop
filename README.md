# Understanding Transformers Workshop

![WorkshopBanner](extra_material/workshop_banner.png)

Hello! Thank you for your interest in our transformer workshop!

In this workshop we will act as a synthesizer of various online resources and materials shared by the broader AI community.

The prerequisites are the ability to read Python and know the basics of Calculus, Probability and Statistics. It is helpful if you are acquainted with PyTorch and Neural Networks, but these latter aspects are not a must.

During the first day, we will focus on theory and applications of transformers. For this we will use slides and writing boards. We will reference all articles and resources from which useful material was taken at the bottom of each slide. This way you can read the articles behind each slide and get a broader understanding in your own spare time after the workshop.

The second day will be a practical session, where we will investigate the code pre-written in a Jupyter Notebook. The Jupyter Notebook was generated using the resources from Andrej Karpathy, which we highly recommend. Please check out https://github.com/karpathy/nanoGPT and https://github.com/karpathy/ng-video-lecture in particular if you wish to review and expand later some of the things we'll discuss during the workshop.

We will go step-by-step through the slides and through the Jupyter Notebook code, explaining things at a deeper level, in order to get an intuitive understanding of how transformers are designed and how they generally work.

Since the audience has varying levels of familiarity with the prerequisites, this workshop uses a dual-track approach: we'll consistently parallel the code with Figure 1 from the "Attention is All You Need" paper, by Vaswani et al. Note that this paper and the snipped Figure 1 block diagram are already available within the `extra_material/` folder for convenience. You will also find the theory presentation in [PDF](extra_material/PresentationAllFormats/UnderstandingTransformers_Workshop_2026_Final.pdf) and [PowerPoint](extra_material/PresentationAllFormats/UnderstandingTransformers_Workshop_2026_Final.pptx) formats inside the `extra_material/PresentationAllFormats/` folder. In addition to the references on the slides and in the reference section at the end, the PowerPoint presentation includes speaker notes that may contain additional links to papers, videos, and other resources for further study. These notes are not included in the PDF version. The general aim is to allow participants to engage at their own individual comfort level:

* Those proficient in Python, PyTorch, Calculus and Statistics can dive into implementation details.
* Those less familiar with these prerequisites can follow the architecture through the block diagram, gaining an intuitive understanding of component functionality and interactions.

Everyone will hopefully leave understanding what each component does and how they combine, whether through code-level details or higher-level abstractions.

Please continue with the environment setup instructions below, and see you in the Workshop!

Danu

## Virtual Environment Setup Instructions
Install the virtual environment / venv via: `python -m venv .transformer_workshop`

Activate the virtual environment via: `source .transformer_workshop/bin/activate` 

You should now see a `(.transformer_workshop)` string prepended to your terminal prompt, indicating the environment is active.

Install required modules via: `pip install -r requirements.txt`

## Using the Jupyter Notebook within Visual Studio Code directly

If you don't have Visual Studio Code / VS Code installed, you can get it from: https://code.visualstudio.com/ 

To avoid setting up a Jupyter Notebook kernel yourself, we recommend opening this repository folder as **the uppermost folder in VS Code**, i.e. as a root workspace folder, and you should be able to use the virtual environment for running the code, i.e. no separate manual installation of the jupyter kernel will be required, because VS Code should do it automatically for you in the background, after asking you for permissions. 

Within VS Code directly, open `mini_gpt.ipynb` and on the top-right corner you will see a `Select Kernel` option. After clicking that, a drop-down menu will appear, where you should select `Python Environments` You should then see the `.transformer_workshop` as one of the listed options. Select it and click on the `Run All` button to sequentially execute all cells in the notebook. Note that in case you didn't install all the requirements, you might see the prompt: "Running cells with '.transformer_workshop (Python 3.x.y)' requires the ipykernel package." Click on `Install`.

If there are no runtime errors after clicking the aforementioned `Run All`, then everything was installed properly and you're all set.

## Using the Jupyter Notebook in the browser instead of VS Code
Alternatively, you can bypass the traditional code editors altogether and open the Jupyter Notebook in the browser.

First, setup a kernel via: 

`python -m ipykernel install --user --name .transformer_workshop --display-name "TransformerWorkshop"`

Run the Jupyter Notebook start command in the terminal: `jupyter notebook` At this point you should see many lines printed in the terminal and if you scroll through them there should be a `localhost` URL containing a `token=` parameter as part of it. By opening it in the browser, you will see a list of all the repository content, including **mini_gpt.ipynb**. Double click on it.

A page will open with the code for mini-gpt. Select the correct kernel name from the dropdown list on the right side of the page, e.g. "TransformerWorkshop" or any other string you may have specified earlier with the `--display-name` argument.

If everything was set up correctly in the previous steps, you should be able to run the import statements in the first notebook cell and not get any dependency errors. To run a cell you can click the triangle/"play" button, however your browser may offer other convenient keyboard shortcuts for this.

If imports work, run all the other cells to see if you don't get any other runtime errors.

To terminate the Jupyter Notebook session press Ctrl+C and confirm with the "yes"/"y" option.

To deactivate the virtual environment, simply type: `deactivate` in the terminal.

## Beyond this workshop

Please note that, for simplicity, the `mini_gpt.ipynb` notebook uses character-level tokenization, where each character is a separate token. As a natural next step after the workshop, you can explore our [Understanding Tokenization repository](https://github.com/ducspe/UnderstandingTokenization) to expand on what you have learned and discover other tokenization methods, including byte pair encoding (BPE).

## Acknowledgments

This workshop was made possible with the help of the following institutions:
- Helmholtz Center Hereon, Geesthacht, Germany
- Helmholtz AI

This work was supported by the Helmholtz Association Initiative and Networking Fund through the Helmholtz AI [grant number: ZT-I-PF-5-01].