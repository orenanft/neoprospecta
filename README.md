#DESAFIO PARA DESENVOLVEDOR FULL STACK
##DESCRIÇÃO:
Seguem as instruções do teste para a posição de Desenvolvedor Full Stack na
Neoprospecta Microbiome Technologies.
O deadline para entrega é dia 7 dias após recebimento deste e-mail a resposta da
Neoprospecta deverá ser dada no máximo durante os próximos 10 dias.
O objetivo do teste é analisar sua familiaridade com o Django, Django Rest Framework
(DRF), Angular, SCSS, HTML e práticas de programação.
##REQUISITOS:
Deve ser construída uma aplicação para listar e editar clientes utilizando ​ Angular 8+
e outra em Django 2+.
O Frontend em Angular deve interagir com o Backend por meio de uma API REST em
Django, para exibir e permitir editar uma lista de clientes.
* RF01 ​ - Criar endpoint no Backend para o Frontend consultar (​ GET​ ) deve ser como esse
exemplo: ​ http://private-92a969-processoseletivo1.apiary-mock.com/customers​ ;
* RF02 ​ - A população dos dados para esse endpoint deve ser feita manualmente via SQL ou
ORM.
* RF03 ​ - Deve ser feito uma listagem de clientes apresentada em forma de “​ tabela​ ” quando a
tela for maior ou igual a 768px e em forma de “​ cards​ ” quando a tela for menor que 768px;
* RF04 ​ - A listagem deve ser ordenável e filtrável ​ server side ​ por Id, nome, idade e cidade;
* RF05 ​ - A listagem deve possuir paginação ​ server side ​ a cada 10 clientes;
* RF06 ​ - Deve haver um botão de “editar” cliente em cada linha da tabela;
* RF07 ​ - Ao clicar no botão de “editar” o usuário deve ser redirecionado para uma outra rota com
os dados do cliente em formato editável;
* RF08 ​ - Deve ser adicionado na tela de edição um botão de “salvar” e um de “cancelar”;
* RF09 ​ - Ao clicar no botão de “salvar” os dados atualizados do cliente devem ser enviados
(​ PUT​ ) ​ para um endpoint de edição do cliente. Conforme este exemplo:
“https://private-92a969-processoseletivo1.apiary-mock.com/customers/{id_do_cliente}/”;
* RF10 ​ - Sendo que, depois do retorno da requisição (​ PUT​ ) o usuário deve ser redirecionado
para listagem e a aplicação deve apresentar a ele uma notificação dizendo “Cliente
{nome_do_cliente} atualizado com sucesso!”;REQUISITOS NÃO FUNCIONAIS:
* RNF01​ - A aplicação deve ser hospedada em algum servidor de sua preferência, podendo ser
Python Any Where, Github Pages ou onde você achar melhor;
* RNF02 ​ - O código fonte deve ser publicado no GitHub e o link deverá ser enviado como
resposta deste e-mail;
* RNF03 ​ - Deve ser utilizado SASS na estilização.
BÔNUS:
* RF11​ - Adicionar um validador reativo no input de idade para tamanho de no mínimo 1 e
máximo de 3 números (ReactiveFormsModule). Este validador só é acionado se o usuário tocar
no campo. Caso o usuário digite algum valor que seja errado o botão de salvar deve ficar
desabilitado;
* RNF04 ​ - Adicionar testes unitários nos principais componentes de frontend;
* RNF05 ​ - Adicionar testes nos endpoints;
* RNF06 ​ - Utilizar docker.
##OBSERVAÇÕES:
Pode utilizar as ferramentas que achar melhor. A utilização de angular-cli e
django-admin são opções sua porém são fortemente recomendados pela facilidade no build
embora seja possível atingir o mesmo efeito com outras ferramentas.
Desejamos sucesso em seu teste desde já! Nos colocamos a disposição para
esclarecer quaisquer dúvidas.
Links para auxílio:
https://www.djangoproject.com/start/
https://angular.io/docs/ts/latest/quickstart.html
