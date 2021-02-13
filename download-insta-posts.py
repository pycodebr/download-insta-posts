from datetime import datetime
import instaloader

# Carrega a lib e faz login com a conta desejada #
L = instaloader.Instaloader()
L.login('*** SEU USER DO INSTA ***', '*** SUA SENHA ***')

# Carrega todos os posts do perfil escolhido #
posts = instaloader.Profile.from_username(L.context, "pycodebr").get_posts()

# Período que deseja baixar os Posts #
SINCE = datetime(2021, 1, 16)
UNTIL = datetime(2021, 1, 18)

# Percorre os posts e baixa apenas os que estão dentro do período desejado #
for post in posts:
    if (post.date >= SINCE) and (post.date <= UNTIL):
        print(post.date)
        L.download_post(post, "insta-posts-downloads")