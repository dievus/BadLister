# BlackLister - A Wordlist Generator for Password Deny List Filtration

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M03Q2JN)

<p align="center">
  <img src="https://github.com/dievus/BlackLister/blob/main/images/example.png" />
</p>

I regularly do internal, external, and web application penetration tests where clients struggle with users utilizing common passwords, but do not know how to develop a list to prevent them.

BlackLister is a simple solution for generating these lists. A default list is already available, "example_deny_list.txt," which provides common strings we see in passwords, such as months, years, common password runs, and other common words and numbers. BlackLister will parse the word list provided by the user, and return strings output with "leetspeak," or word combinations where numbers or letters in a string are substituted with special characters and numbers similar to the original string. Depending on the list provided, the results can be quite large, and it is important to customize each list to the associated business.

As an example, if your company is "Acme Corp Inc.," which is located in Ohio, you may want to include "Acme," "Ohio," and "Buckeyes" in the word list. All too often passwords contain the company name, state, city, or local sports team, and these passwords are incredibly easy to predict or crack. 

## Usage
To run the tool, simply run `python3 blacklister.py` and input a filename when prompted to. The tool was developed in Windows, which makes directory parsing a bit of a pain, so it is recommended to include the word list in the same directory as blacklister.py. Once BlackLister has been run, a new file named `denylist_passwords.txt` can be utilized in whichever way the user wishes. Additionally, the user can output the file contents to terminal, if desired, by pressing `y` when asked.
