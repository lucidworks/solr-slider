Lucidworks Solr on YARN via Slider
========

Solr on YARN - Slider package for deploying SolrCloud to a YARN cluster.

Getting Started
========

Follow the instructions for getting started with Slider:
http://slider.incubator.apache.org/docs/getting_started.html

Be sure to add the $SLIDER_HOME/bin directory to your path.

Throughout these instructions, $PROJECT_HOME refers to the directory where you cloned this project.

**1) Start ZooKeeper 3.4.6+ on your local workstation**

Running Solr with embedded ZooKeeper is not supported. Take note of the ZooKeeper connection string as you'll need to include it in the Solr deployment metadata below.

**2) Download a Solr distribution archive (tgz)**

Download the latest Solr distribution from: http://lucene.apache.org/solr/downloads.html

Once downloaded, move the distribution archive to `$PROJECT_HOME/package/files/solr.tgz`

The distribution archive must be named `solr.tgz` as the `metainfo.xml` file references this path.

**3) Create the solr-on-yarn.zip deployment package**

Create the Slider package using zip:

```
zip -r solr-on-yarn.zip metainfo.xml package/
```

**4) Install the package on HDFS**

```
slider install-package --replacepkg --name solr --package $PROJECT_HOME/solr-on-yarn.zip
```

**5) Configure environment specific settings**

Edit the `$PROJECT_HOME/appConfig-default.json`. At a minimum, you'll need to update the following settings to match your environment:

```
    "java_home": "/Library/Java/JavaVirtualMachines/jdk1.7.0_67.jdk/Contents/Home",
    "site.global.app_root": "${AGENT_WORK_ROOT}/app/install/solr-5.2.0",
    "site.global.zk_host": "localhost:2181",
```

Review the other settings in this file to verify they are correct for your environment.

6) Configure the number of Solr nodes to deploy

Edit `yarn.component.instances` in `resources-default.json` to set the number of Solr nodes to deploy across your cluster.

7) Deploy Solr on YARN

```
slider create solr --manager $YARN_MANAGER \
  --template $PROJECT_HOME/appConfig-default.json \
  --resources $PROJECT_HOME/resources-default.json
```

where `$YARN_MANAGER` is the host and port of the YARN resource manager, such as localhost:8032.

8) Navigate to the YARN ResourceManager Web UI

Also, you can get the URL of each Solr instance by consulting the Slider registry (so you can reach the Solr Web Admin UI) by doing:

```
slider registry --name solr --getexp servers --manager $YARN_MANAGER
```

You can get the ZooKeeper connection string used by Solr by doing:

```
slider registry --name solr --getexp zookeeper --manager $YARN_MANAGER
```

NOTE: The registry command requires using Java 7 as there's a bug in Slider that prevents the registry command from working correctly,
see: https://issues.apache.org/jira/browse/SLIDER-878
