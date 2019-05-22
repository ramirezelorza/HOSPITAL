<?php
 // $Id$
 //
 // Authors:
 // 	Jeff Buchbinder <jeff@freemedsoftware.org>
 //
 // FreeMED Electronic Medical Record and Practice Management System
 // Copyright (C) 1999-2012 FreeMED Software Foundation
 //
 // This program is free software; you can redistribute it and/or modify
 // it under the terms of the GNU General Public License as published by
 // the Free Software Foundation; either version 2 of the License, or
 // (at your option) any later version.
 //
 // This program is distributed in the hope that it will be useful,
 // but WITHOUT ANY WARRANTY; without even the implied warranty of
 // MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 // GNU General Public License for more details.
 //
 // You should have received a copy of the GNU General Public License
 // along with this program; if not, write to the Free Software
 // Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

// Handle public methods for initialization
include_once( dirname(__FILE__) . "/lib/freemed.php" );

define( 'LOG4PHP_CONFIGURATION', dirname(__FILE__) . "/data/config/log4php.xml" );
define( 'GWTPHP_FORCE_SHOEHORN', true );
define( 'FORCE_CAST_TO_PHP_PRIMITIVE_TYPES', true );

include_once( LOG4PHP_DIR . '/LoggerManager.php' );
include_once( GWTPHP_DIR . '/RemoteServiceServlet.class.php' );

GWTPHPContext::getInstance()->setServicesRootDir( dirname(__FILE__) . '/lib/' );
GWTPHPContext::getInstance()->setGWTPHPRootDir( dirname(__FILE__) . "/lib/gwtphp/" );

$servlet = CreateObject( 'org.freemedsoftware.core.AuthenticatedRemoteServiceServlet' );
$servlet->start();

?>
