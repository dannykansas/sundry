#!/usr/bin/perl
 
# test_mod_evasive.pl: small script to test mod_dosevasive's effectiveness
 
use IO::Socket;
use strict;
 
for(0..100) {
  my($response);
  my($SOCKET) = new IO::Socket::INET( Proto   => "tcp",
                                      PeerAddr=> "puppet.mysidewalk.com:80");
  if (! defined $SOCKET) { die $!; }
  print $SOCKET "GET /?$_ HTTP/1.0nn";
  $response = <$SOCKET>;
  print $response;
  close($SOCKET);
}
