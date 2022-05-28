FROM php:7.1-apache

RUN apt update \
#    && pecl install amqp-1.9.4 \
#    && pecl install apcu-5.1.18 \
    && pecl install redis-5.1.1

COPY src /var/www/html/
EXPOSE 80