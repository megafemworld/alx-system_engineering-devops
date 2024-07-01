# install python pip3 flask
package { 'flask':
  ensure => '2.1.0',
  provider => 'pip3',
  require => package['python3-pip'],
}
