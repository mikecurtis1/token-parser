FROM httpd:2.4

# Enable proxy modules
RUN sed -i \
    -e 's/#LoadModule proxy_module/LoadModule proxy_module/' \
    -e 's/#LoadModule proxy_http_module/LoadModule proxy_http_module/' \
    conf/httpd.conf

# Copy extra proxy config
COPY proxy.conf /usr/local/apache2/conf/extra/proxy.conf

# Include the extra proxy config
RUN echo "Include conf/extra/proxy.conf" >> /usr/local/apache2/conf/httpd.conf