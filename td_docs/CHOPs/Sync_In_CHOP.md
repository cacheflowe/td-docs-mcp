---
url: https://docs.derivative.ca/Sync_In_CHOP
category: CHOPs
title: Sync_In_CHOP
---

# Database error

A database query error has occurred. This may indicate a bug in the software.

[577d99f7aa047be7f96d2ccd] /Sync_In_CHOP Wikimedia\Rdbms\DBQueryError: A database query error has occurred. Did you forget to run your application's database schema updater after upgrading or after adding a new extension?

Please see https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:Upgrading and https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:How_to_debug for more information.

Error 1205: Lock wait timeout exceeded; try restarting transaction

Function: Wikimedia\Rdbms\Database::delete

Query: DELETE FROM `ed_url_cache` WHERE url = 'https://docs.derivative.ca/api.php?action=query&list=categorymembers&cmtitle=Category:CHOPs&format=xml&cmlimit=500:array (\n \'timeout\' => \'default\',\n \'HTTPTimeout\' => 25,\n \'HTTPConnectTimeout\' => 5.0,\n \'postData\' => NULL,\n)'

Backtrace:

from /var/www/html/includes/libs/rdbms/database/Database.php(1618)

#0 /var/www/html/includes/libs/rdbms/database/Database.php(1602): Wikimedia\Rdbms\Database->getQueryException()

#1 /var/www/html/includes/libs/rdbms/database/Database.php(1576): Wikimedia\Rdbms\Database->getQueryExceptionAndLog()

#2 /var/www/html/includes/libs/rdbms/database/Database.php(952): Wikimedia\Rdbms\Database->reportQueryError()

#3 /var/www/html/includes/libs/rdbms/database/Database.php(2093): Wikimedia\Rdbms\Database->query()

#4 /var/www/html/includes/libs/rdbms/database/DBConnRef.php(103): Wikimedia\Rdbms\Database->delete()

#5 /var/www/html/includes/libs/rdbms/database/DBConnRef.php(549): Wikimedia\Rdbms\DBConnRef->__call()

#6 /var/www/html/extensions/ExternalData/includes/connectors/traits/EDConnectorCached.php(157): Wikimedia\Rdbms\DBConnRef->delete()

#7 /var/www/html/extensions/ExternalData/includes/connectors/traits/EDConnectorCached.php(88): EDConnectorHttp->cache()

#8 /var/www/html/extensions/ExternalData/includes/connectors/EDConnectorHttp.php(152): EDConnectorHttp->callCached()

#9 /var/www/html/extensions/ExternalData/includes/EDParserFunctions.php(93): EDConnectorHttp->run()

#10 /var/www/html/extensions/ExternalData/includes/EDParserFunctions.php(116): EDParserFunctions::get()

#11 /var/www/html/extensions/ExternalData/includes/ExternalDataHooks.php(21): EDParserFunctions::fetch()

#12 /var/www/html/includes/parser/Parser.php(3442): ExternalDataHooks::{closure}()

#13 /var/www/html/includes/parser/Parser.php(3125): Parser->callParserFunction()

#14 /var/www/html/includes/parser/PPFrame_Hash.php(276): Parser->braceSubstitution()

#15 /var/www/html/includes/parser/Parser.php(3316): PPFrame_Hash->expand()

#16 /var/www/html/includes/parser/PPFrame_Hash.php(276): Parser->braceSubstitution()

#17 /var/www/html/includes/parser/Parser.php(2954): PPFrame_Hash->expand()

#18 /var/www/html/includes/parser/Parser.php(1609): Parser->replaceVariables()

#19 /var/www/html/includes/parser/Parser.php(723): Parser->internalParse()

#20 /var/www/html/includes/content/WikitextContentHandler.php(301): Parser->parse()

#21 /var/www/html/includes/content/ContentHandler.php(1721): WikitextContentHandler->fillParserOutput()

#22 /var/www/html/includes/content/Renderer/ContentRenderer.php(47): ContentHandler->getParserOutput()

#23 /var/www/html/includes/Revision/RenderedRevision.php(266): MediaWiki\Content\Renderer\ContentRenderer->getParserOutput()

#24 /var/www/html/includes/Revision/RenderedRevision.php(237): MediaWiki\Revision\RenderedRevision->getSlotParserOutputUncached()

#25 /var/www/html/includes/Revision/RevisionRenderer.php(221): MediaWiki\Revision\RenderedRevision->getSlotParserOutput()

#26 /var/www/html/includes/Revision/RevisionRenderer.php(158): MediaWiki\Revision\RevisionRenderer->combineSlotOutput()

#27 [internal function]: MediaWiki\Revision\RevisionRenderer->MediaWiki\Revision\\{closure}()

#28 /var/www/html/includes/Revision/RenderedRevision.php(199): call_user_func()

#29 /var/www/html/includes/poolcounter/PoolWorkArticleView.php(91): MediaWiki\Revision\RenderedRevision->getRevisionParserOutput()

#30 /var/www/html/includes/poolcounter/PoolWorkArticleViewCurrent.php(97): PoolWorkArticleView->renderRevision()

#31 /var/www/html/includes/poolcounter/PoolCounterWork.php(162): PoolWorkArticleViewCurrent->doWork()

#32 /var/www/html/includes/page/ParserOutputAccess.php(299): PoolCounterWork->execute()

#33 /var/www/html/includes/page/Article.php(714): MediaWiki\Page\ParserOutputAccess->getParserOutput()

#34 /var/www/html/includes/page/Article.php(528): Article->generateContentOutput()

#35 /var/www/html/includes/actions/ViewAction.php(78): Article->view()

#36 /var/www/html/includes/MediaWiki.php(541): ViewAction->show()

#37 /var/www/html/includes/MediaWiki.php(321): MediaWiki->performAction()

#38 /var/www/html/includes/MediaWiki.php(902): MediaWiki->performRequest()

#39 /var/www/html/includes/MediaWiki.php(561): MediaWiki->main()

#40 /var/www/html/index.php(50): MediaWiki->run()

#41 /var/www/html/index.php(46): wfIndexMain()

#42 {main}
