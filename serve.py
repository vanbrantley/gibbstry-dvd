from livereload import Server

server = Server()

server.watch("index.html")
server.watch("styles.css")

# Serve the files on port 8888
server.serve(root=".", port=8888)
