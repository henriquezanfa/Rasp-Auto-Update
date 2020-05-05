# Raspberry Auto Update

O objetivo desse repo é gerar um código para utilização em Raspberry's (acredito que funcione em todos os OS, mas só testei com Raspberry) que verifique updates na branch master do git e faça o pull das atualizações, quando houverem.

Isso é útil, entre outros casos, para soltar releases de algum software rodando em raspberry's simultaneamente. 

Pra criar esse script, me baseei [nesse artigo](https://medium.com/@johngrant/updating-distributed-raspberrypis-with-automatic-code-updates-3336aa0bcca1), mas não segui a risca. Para não precisar escrever o login e senha do git no código (como feito no original), fiz algumas configurações no ssh do raspberry, que achei [nesse link](https://amoffat.github.io/sh/tutorials/interacting_with_processes.html#how-you-should-really-be-using-ssh).

Além disso, traduzi pro português a parte do console app e coloquei uma contagem regressiva pra facilitar o entendimento do processo. 

Uma outra possibilidade de uso (meu objetivo inicial) é executar esse script no startup do raspberry para verificar atualizações, não de tempos em tempos, como no exemplo mostrado.
Para isso, retirei o ```while True``` do init e adicionei o script no startup do raspberry (```~/.config/lxsession/LXDE-pi/autostart```)

É importante lembrar que pra funcionar de uma forma legal, você não deve utilizar a branch ```master``` para desenvolvimento e testes, apenas como release de versões já testadas ([git worklow](https://www.atlassian.com/git/tutorials/comparing-workflows)).
