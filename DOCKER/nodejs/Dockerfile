FROM node:latest

RUN npm install -g @angular/cli

WORKDIR /var/www/html/express
EXPOSE 9090

WORKDIR /var/www/html/angular
EXPOSE 9091

WORKDIR /var/www/html/angular_js
EXPOSE 9092

WORKDIR /var/www/html/vue_js
EXPOSE 9093

ENTRYPOINT ["tail", "-f", "/dev/null"]