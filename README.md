# Protótipo do Diretório Piloto de Jornalistas no Brasil

![GitHub repo size](https://img.shields.io/github/repo-size/dauid64/diretorio_jornalistas?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/dauid64/diretorio_jornalistas?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/dauid64/diretorio_jornalistas?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/dauid64/diretorio_jornalistas?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/dauid64/diretorio_jornalistas?style=for-the-badge)

<p align="center">
    <img src="https://github.com/dauid64/diretorio_jornalistas/assets/94979678/eed735eb-c79b-413f-8abc-4885b444d74a" alt="Logo da UnB">
</p>

> A finalidade do DPJB é manter uma base de dados que contenha
informações sobre os jornalistas, assim como as interfaces necessárias a sua manutenção e atualização – nos aspectos técnicos – assim como a alimentação de dados e administração do mesmo por parte de pessoas sem formação em sistemas e computação.

### Requisitos

- [x] Listar Jornalistas
- [x] Procurar Jornalistas
- [x] Cadastrar Jornalista
- [x] Cadastrar Revisor
- [x] Cadastrar Histórico Profissional: incluir referências
- [x] Verificar e aprovar o cadastro de jornalista
- [ ] Cadastrar Obra Jornalistica
- [ ] Cadastrar Associação Jornalistica
- [ ] Verificar e aprovar cadastro da associação

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou a versão mais recente de `< Python >`
- Você tem uma máquina `< Windows / Linux / Mac >`

## 🚀 Instalando DPJB

Para rodar o DPJB é necessário instalar dependências de bibliotecas, siga então as seguintes etapas:

Linux e macOS:
```
python -m venv venv
. venv/bin/activate
cd app
pip install -r requirements.txt
```
Windows:
```
python -m venv venv
cd venv/Scripts
activate
cd app
pip install -r requirements.txt
```

## ☕ Usando DPJB

Para usar o DPJB, siga estas etapas:

* Primeiro você terá que entrar na pastar "dotenv_files" copiar o arquvio ".env-examples" para a mesma pasta com o nome ".env" e configurar como o exemplo suas variáveis de ambiente.

* Entre na pasta "app" e execute o comando com o ambiente virtual ligado `python manage.py migrate` para criar as tabelas em seu banco.

* Após essas etapas você está pronto para começar a utilizar o DPJB, basta executar o comando na pasta app `python manage.py runserver`.

## 👨‍🏫 Orientador

<table>
  <tr>
    <td align="center">
      <a href="http://buscatextual.cnpq.br/buscatextual/visualizacv.do;jsessionid=5E925864A1302E3E6B065741269FC62B.buscatextual_0" title="Lattes">
        <img src="https://github.com/dauid64/diretorio_jornalistas/assets/94979678/b5dee120-150c-4316-8431-b18ad9b277f5" width="100px;" alt="Foto do professor Edison Ishikawa"/><br>
        <sub>
          <b>Edison Ishikawa</b>
        </sub>
      </a>
    </td>
  </tr>
</table>


## 🤝 Desenvolvedores

Às seguintes pessoas contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/dauid64" title="Github">
        <img src="https://github.com/dauid64/streaming_audio/assets/94979678/ca828726-8438-4c20-9227-b2639e13f96d" width="100px;" alt="Foto do Carlos David"/><br>
        <sub>
          <b>Carlos David</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Tais-A" title="Github">
        <img src="https://github.com/dauid64/diretorio_jornalistas/assets/94979678/dc4f301f-b71b-4de7-a6ac-601e28eb1055" width="100px;" alt="Foto da Tais Alves"/><br>
        <sub>
          <b>Tais Alves</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Daltro-Oliveira-Vinuto" title="Github">
        <img src="https://avatars.githubusercontent.com/u/18556262?s=400&u=7cf8646ecf6740c9aab7ca310959f38b68410d9c&v=4" width="100px;" alt="Foto de Daltro Oliveira Vinuto"/><br>
        <sub>
          <b>Daltro Oliveira Vinuto</b>
        </sub>
      </a>
    </td>


  </tr>
</table>