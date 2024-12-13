Berserker Workout
Bem-vindo ao Berserker Workout!
Esta aplicação em modo de linha de comandos (CLI) ajuda-o(a) a gerir treinos, planos, exercícios, acompanhar o seu progresso e ajustar as suas metas de fitness de forma simples e personalizada.

O que há de novo nesta fase?

Introdução de herança e polimorfismo nos treinos (TreinoForca, TreinoCardio, TreinoSuperior, TreinoInferior)
Persistência de dados em ficheiro JSON, garantindo que as suas informações permanecem guardadas entre utilizações
Cálculo de IMC e recomendação calórica, com possibilidade de ajustes (perda rápida, lenta, manter, ganhar massa)
Arte ASCII no arranque, oferecendo uma experiência mais envolvente
Melhor organização interna do código, preparando o projeto para evoluções futuras (por exemplo, uma interface gráfica)

Requisitos:

Ter o Python 3.x instalado no seu sistema
Não são necessárias outras bibliotecas além das fornecidas pela instalação padrão do Python

Como Executar:

Extraia todos os ficheiros do projeto para uma pasta local.
Certifique-se de que a estrutura está intacta (a pasta "classes/" contém os ficheiros de classe).

Abra um terminal/linha de comandos nessa pasta.

Execute:

python main.py

Ou, se necessário:

python3 main.py

Ao iniciar, verá uma arte ASCII e será recebido com o "Menu Principal".

Primeiros Passos:
No "Menu Principal" terá opções:

Criar Novo Utilizador
Login
Visualizar Utilizadores Existentes
Sair
Criar Novo Utilizador (opção 1):

Introduza um nome de utilizador (sem espaços nem acentos, apenas letras, números ou underscore).
Defina uma senha.
Forneça o seu nome completo, idade, peso e altura.
Escolha o objetivo: perder peso, manter peso e tonificar, ou ganhar massa muscular.
No final, terá um novo utilizador registado.
Login (opção 2):

Introduza o nome de utilizador e a senha que criou.
Se os dados estiverem corretos, entrará no menu do utilizador.
Dentro do Menu do Utilizador:
Terá várias opções, como:

Calcular IMC e Calorias Recomendadas

Apresenta o seu IMC e permite ajustar a recomendação calórica diária consoante as suas metas (por exemplo, perda rápida reduz mais calorias ao valor base).
Gerir Planos

Criar novo plano de treino com um nome e um período (ex.: "Plano de 1 mês").
Adicionar treinos a esse plano (Força, Cardio, Superior, Inferior) e decidir se quer inserir exercícios de imediato.
Visualizar e editar o plano, incluindo remover ou renomear treinos.
Visualizar Histórico

Ver todos os treinos que finalizou, incluindo data, dificuldade, calorias queimadas e exercícios realizados.
Editar Perfil

Alterar idade, peso, altura ou objetivo, mantendo os seus dados atualizados.
Calcular Calorias Diárias (Objetivo Atual)

Ver a recomendação calórica base, sem ajustes extra, de acordo com o seu objetivo definido.
Logout

Retornar ao Menu Principal.
Em qualquer altura, pode sair completamente da aplicação escolhendo "4. Sair" no Menu Principal. Ao sair, os seus dados (utilizadores, planos, histórico) são guardados num ficheiro JSON ("utilizadores.json"), garantindo que tudo permanece salvo para a próxima vez que iniciar o programa.

Boas Práticas:
Ao criar o utilizador, use um nome de utilizador simples e fácil de lembrar.
Atualize o seu perfil quando necessário, caso o seu peso ou objetivo mude.
Crie planos de treino realistas e adicione exercícios personalizados, tornando o seu plano mais adaptado às suas necessidades.
Finalize os treinos após realizá-los e verifique o histórico para acompanhar o seu progresso ao longo do tempo.

Preparação para o Futuro:
Esta fase 2 prepara o terreno para funcionalidades futuras, como:

Integração com uma interface gráfica mais completa
Recomendação de exercícios mais inteligentes com base no seu histórico
Evolução da persistência de dados para uma base de dados mais robusta

Em caso de Dúvidas:
Se tiver alguma dificuldade, releia este README, siga as instruções passo a passo e explore os menus com calma. O objetivo é tornar a experiência intuitiva e eficiente, ajudando-o(a) a acompanhar o seu progresso de fitness.

Suporte:
Em caso de dúvidas ou problemas, contacte: ralfe.mendes@hotmail.com
Terei todo o gosto em ajudar!

Bom treino e bom progresso com a Berserker Workout!