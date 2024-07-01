# This Puppet manifest installs Flask version 2.1.0 using pip3

# Ensure Python pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0 using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/bin', '/usr/bin'],
  require => Package['python3-pip'],
}
