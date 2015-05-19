Lucidworks Solr on YARN via Slider
========

Solr on YARN - Slider package for deploying SolrCloud to a YARN cluster.

Getting Started
========

Follow the instructions for getting started with Slider:
http://slider.incubator.apache.org/docs/getting_started.html

Throughout these instructions, $PROJECT_HOME refers to the directory where you cloned this project.

1. Start ZooKeeper 3.4.6+ on your local workstation

Running Solr with embedded ZooKeeper is not supported. Take note of the ZooKeeper connection string as you'll need to include it in the Solr deployment metadata below.

2. Download a Solr distribution archive (tgz) from http://lucene.apache.org/solr/downloads.html

Copy the downloaded Solr distribution archive to the $PROJECT_HOME/package/files directory.

3. Create the solr-on-yarn.zip

Create the Slider package using zip:

```
zip -r solr-on-yarn.zip metainfo.xml package/
```

4. Install the package on HDFS

```
$SlIDER_HOME/bin/slider install-package --replacepkg --name solr --package $PROJECT_HOME/solr-on-yarn.zip
```

where $SLIDER_HOME is the location where you installed Slider.

5. Configure environment specific settings

Edit the $PROJECT_HOME/appConfig-default.json. At a minimum, you'll need to update the following settings to match your environment:

```
    "java_home": "/Library/Java/JavaVirtualMachines/jdk1.7.0_67.jdk/Contents/Home",
    "site.global.app_root": "${AGENT_WORK_ROOT}/app/install/solr-5.2.0-SNAPSHOT",
    "site.global.zk_host": "localhost:2181",
```

Review the other settings to verify they are correct for your environment.

6. Configure the number of Solr nodes to deploy

Edit `yarn.component.instances` in resources-default.json to set the number of Solr nodes to deploy across your
cluster.

7. Deploy Solr on YARN

```
bin/slider create solr --manager $YARN_MANAGER --template $PROJECT_HOME/appConfig-default.json --resources $PROJECT_HOME/resources-default.json
```

where $YARN_MANAGER is the host and port of the YARN resource manager, such as localhost:8032.

8. Navigate to the YARN ResourceManager Web UI @ http://localhost:8088/cluster

Also, you can get the location of a Solr endpoint by consulting the Slider registry (so you can reach the Solr Web Admin UI) by doing:

```
bin/slider registry --name solr --getexp servers --manager localhost:8032
```

NOTE: This requires using Java 7 as there's a bug in Slider that prevents the registry command from working correctly,
see: https://issues.apache.org/jira/browse/SLIDER-878
