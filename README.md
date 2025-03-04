# Welcome to the Large Language Model Testing System!

**2025.03.03**

The Large Language Model Testing System is a system based on artificial intelligence technology, primarily used to evaluate and test the capabilities of large language models. The system simulates text-based and multiple-choice question environments to ensure that their performance in specialized fields meets expectations.

## Instructions for Use

You need to first download Ollama to call the model locally or remotely. This project uses API calls. Please update your API address in `model_ask.py` and `model.py`, and modify the model and corresponding prompt as needed.

This project uses the Flask framework. You can start the web page by running the `1.py` file. Note that you need to install Flask and other libraries via pip.

The system supports uploading Excel files to automatically answer questions and generate answers. You can also call the large language model again to evaluate the quality of the response.

The system supports two types of tests: text-based questions and multiple-choice questions. The template for the test file can be seen at the bottom of the web page. Please fill in the content strictly according to the template to avoid unexpected errors. Thank you!

The system distinguishes files and their results by file names. "_t" indicates that the file contains the results of text-based questions, "_c" indicates the results of multiple-choice questions, "_r" indicates the evaluation results, and "_a" indicates the answer results. The files you upload will be saved in the "Uploaded Files" section (Note! If your uploaded file contains "_a" or "_r" characters, it will not be displayed in the "Uploaded Files" section but will be shown in the "Answer Results" or "Evaluation Results" section. It is recommended that you rename the file by removing these characters). "_a" files are saved in the "Answer Results" section, and "_r" files are saved in the "Evaluation Results" section.

Recommended usage process: Prepare your questions or multiple-choice questions along with their standard answers, fill them into the Excel file according to the format, upload the file, and click "Model Answer" to generate answers automatically. Click "Model Evaluation" to generate evaluation results automatically.

If you encounter any bugs, please let me know. Your understanding is appreciated!

# 欢迎来到大语言模型测试系统！

**2025.03.03**

大语言模型测试系统‌是一种基于人工智能技术的系统，主要用于评估和测试大语言模型的能力。该系统模拟文字题和选择题环境确保其在专业领域的表现符合预期。
  
## 使用须知

您需要首先下载Ollama以本地或远程调用模型，本项目采用API调用，请在model_ask.py和model.py中更改您的API地址，同时根据您的需要修改模型和相应的提示词。

本项目使用Flask框架，您可以通过运行1.py文件启用网页，注意通过pip安装Flask等库。

该系统支持上传Excel格式的文件，对您的问题自动化作答，生成答案。同时，您可以再次调用大语言模型，对作答模型回答的质量进行评判。

该系统支持选择题和文字题两种形式的测试，测试文件的模板在网页页面下方可见。请您严格按照模板填写内容，避免出现不可预料的错误，谢谢！

该系统以文件名区分文件与文件结果，"_t"表示该文件为文字题结果，"_c"表示该文件为选择题结果，"_r"表示该文件为评测结果，"_a"表示该文件为回答结果。您上传的文件将保存在“上传文件”中(注意！如果您上传的文件含有_a/_r字符，将不会在“上传文件”中显示，但会在“回答结果”或“评测
结果”中显示，推荐您修改文件名，删除这些字符)，"_a"文件保存在“回答结果”中，"_r"文件保存在“评测结果”中。

推荐的使用流程：准备好问题或者选择题与它们的标准答案，按照格式填写Excel文件中，上传文件，根据你的需求，点击模型回答，模型回答将自动生成答案，点击模型评测，模型评测将自动生成评测结果。

如果有bug，请告知我，敬请谅解！
