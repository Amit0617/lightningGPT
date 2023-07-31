# lightningGPT
Get assisted or ask for help for operating lightning client within console

### StartUp
```bash
lightning-cli plugin start /path/to/lightningGPT/lightningGPT.py
```

### Usage
Currently there are two options in the roadmap
1.  ```bash
    lightning-cli helpGPT "Your query you want to ask help for operating lightning node."
    ```

For helping with errors faced during operating `lightningd` by taking logs from stdin.  

2.  ```bash
    lightning-cli adviceGPT
    ```

### Stop
```bash
lightning-cli plugin stop /path/to/lightningGPT/lightningGPT.py
```

### How it works?
It is currently trained on [cln-cheatsheet](https://github.com/grubles/cln-cheatsheet) and [lightning FAQ](https://lightning.readthedocs.io/FAQ.html) section.

It is currently in MVP stage, for future references embeddings will be created for the markdown files of lightning [docs](https://github.com/ElementsProject/lightning/tree/master/doc). And only relevant section (by converting question into embedding and finding cosine similarity between the question and docs embeddings) would be used for prompting the GPT.