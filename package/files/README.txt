Place the Solr distribution archive (.tgz) into this directory and then update the site.global.app_root setting in appConfig-default.json,
e.g. if you put solr-5.2.0-SNAPSHOT.tgz into the files directory, then you would set app_root to:

"site.global.app_root": "${AGENT_WORK_ROOT}/app/install/solr-5.2.0-SNAPSHOT"
