# install python pip3 flask

package { 'python3-pip':
  ensure => installed,
}

package { 'Flask':
  ensure => '2.1.0',
  provider => 'pip3',
  require => package['python3-pip'],
}
