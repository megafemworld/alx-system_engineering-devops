# 1-install_a_package.pp

# Ensure Python pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

