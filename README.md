# SPRINT 04 - ESR1
---

## Alunos

- Deivison Pertel – **RM 550803**
- Eduardo Akira Murata – **RM 98713**
- Guilherme Jacob Soares da Costa – **RM 84581**
- Fabrizio El Ajouri Romano – **RM 550410**
- Wesley Souza de Oliveira – **RM 97874**

---

# LifeSustent - Monitoramento Ambiental
Este código implementa um programa de monitoramento ambiental em tempo real chamado LifeSustent. O programa permite ao usuário verificar a qualidade da umidade do ar, o nível de monóxido de carbono e o volume sonoro em uma determinada cidade.

---

## Funções
### Função transmitir_mensagem_umidade(umidade)
Esta função recebe um valor de umidade como entrada e retorna uma mensagem relacionada à umidade do ar.

Se a umidade for maior que 80, a função retorna: "A umidade está alta. Certifique-se de se manter hidratado."
Se a umidade estiver entre 50 e 80 (inclusive), a função retorna: "A umidade está em um nível ideal. Aproveite o dia!"
Se a umidade estiver entre 20 e 50 (exclusive), a função retorna: "A umidade está em um nível de atenção."
Caso contrário, se a umidade for menor que 20, a função retorna: "A umidade está baixa. É um nível compatível com o do Deserto do Saara, por exemplo. Tenha cuidado com o ressecamento da pele."

---

### Função transmitir_mensagem_monoxido(monoxido)
Esta função recebe um valor de monóxido de carbono como entrada e retorna uma mensagem relacionada à qualidade do ar.

Se o valor de monóxido de carbono for maior ou igual a 50, a função retorna: "Há níveis perigosos de monóxido de carbono no ar. Evite a exposição prolongada."
Se o valor de monóxido de carbono estiver entre 30 e 50 (exclusive), a função retorna: "Há uma quantidade moderada de monóxido de carbono no ar. Mantenha-se atento."
Caso contrário, se o valor de monóxido de carbono for menor que 30, a função retorna: "A quantidade de monóxido de carbono está dentro dos níveis seguros."

---

### Função transmitir_mensagem_volume(volume)
Esta função recebe um valor de volume sonoro como entrada e retorna uma mensagem relacionada ao volume.

Se o volume for maior ou igual a 85, a função retorna: "O volume está muito alto. Proteja seus ouvidos utilizando protetores auriculares."
Se o volume estiver entre 60 e 85 (exclusive), a função retorna: "O volume está em um nível moderado. Aprecie a música!"
Caso contrário, se o volume for menor que 60, a função retorna: "O volume está dentro dos limites seguros."

---

### Função verifica_num(frase)
Esta função recebe uma frase como entrada e solicita ao usuário que digite um número. Ela verifica se o valor inserido é um número válido e retorna o número inteiro. Caso o valor inserido não seja um número válido, a função solicita novamente a entrada do usuário até que um número seja fornecido.

---

### Função register(register_dic)
Esta função serve para pegar os dados cadastrais do usuario, passando por todas as chaves, através de um loop e caso uma das chaves seja um dicionario(dict), ele executa a função denovo neste dicionario, assim, percorrendo todas as chaves do dicionario que está no parâmetro.

---

### Função login(register)
Esta função serve exclusivamente para realizar o login do usuário no sistema, sendo executada após a função register(register_dic), assim pegando o retorno dessa função e comparando se o e-mail inserido e a senha, são os mesmos de quando realizado o cadastro.


---

### Função leave(mensagem, options)
Esta função é usada para a parte final do código, onde o usuário terá duas opções, essas duas opções será inserida no parâmetro "options", e a mensagem de input sera inserida no parâmetro "mensagem", a função tem como objetivo forçar o usuário a escolher uma opção entre as sugeridas.

---


## Fluxo do programa
O programa inicia depois exibe uma mensagem de boas-vindas e explica o propósito do serviço após isso, solicita ao usuário para criar um cadastro para ele poder acessar o serviço, são solicitados os dados do usuário (nome, idade, e-mail, cidade, número de telefone, estado, senha, nome da rua, número da rua, CEP). Caso contrário, o programa prossegue sem solicitar esses dados.

Em seguida, o programa pede para que o usuario faça login, utilizando o e-mail e a senha. Após isso, inicia-se um loop no qual o usuário pode realizar análises do ambiente.

Dentro do loop, são solicitadas as condições ambientais (umidade do ar, nível de monóxido de carbono e volume sonoro) por meio da função verifica_num(). Em seguida, são transmitidas mensagens relacionadas a essas condições usando as funções transmitir_mensagem_umidade(), transmitir_mensagem_monoxido() e transmitir_mensagem_volume(). As mensagens são exibidas na tela.

Depois disso, o programa pergunta ao usuário se ele deseja realizar outra análise ou sair. Se a resposta for "V", o loop continua e uma nova análise pode ser feita. Se a resposta for "S", o loop é interrompido e uma mensagem de saída é exibida agradecendo-o por usar o serviço.
