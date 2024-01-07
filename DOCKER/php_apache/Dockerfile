FROM php:8.1-apache

RUN echo 'deb [trusted=yes] https://repo.symfony.com/apt/ /' | tee /etc/apt/sources.list.d/symfony-cli.list \
    && apt-get update --fix-missing && apt-get install -y \
        git-core \
        git \
        unzip \
        curl \
        wget \
        nano \
        libonig-dev \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        libxml2-dev \
        libcurl4-openssl-dev \
        libpq-dev \
        make \
        symfony-cli \
    && pecl install xdebug \    
    && docker-php-ext-enable xdebug \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) gd mbstring xml curl pdo pdo_mysql pdo_pgsql sockets

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php composer-setup.php \
    && rm composer-setup.php \
    && mv composer.phar /usr/local/bin/composer

RUN curl -1sLf 'https://dl.cloudsmith.io/public/symfony/stable/setup.deb.sh' | bash -E \
    && apt install -y symfony-cli

COPY apache/ports.conf /etc/apache2
COPY apache/000-default.conf /etc/apache2/sites-available

RUN a2enmod rewrite && service apache2 start

ENTRYPOINT ["tail", "-f", "/dev/null"]