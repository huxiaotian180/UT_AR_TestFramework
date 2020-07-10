node('docker') {

   stage 'Env'
       sh "rm -rf UT_AR_Test*"
       sh "mkdir UT_AR_TestFramework"

   stage 'Checkout'
       dir('UT_AR_TestFramework'){
       git credentialsId: 'a124189f-da35-4362-897f-0ddcc90328e0', url: 'https://gitlab.aishu.cn/anyrobot/UT_AR_TestFramework.git', branch: '${BRANCH_NAME}'
 
   stage 'Gen Version'
       def atversion = load("at-version/atversion.groovy")
       def at_version = atversion.get_version_revision()

   stage 'Build Images'
       sh "rm -rf ./.git"
       sh "tar zcvf UT_AR_TestFramework.tar.gz *"
       sh "mv UT_AR_TestFramework.tar.gz ./docker/"
       sh "docker build --no-cache -t 192.168.84.23:5000/${BRANCH_NAME}/anyrobot-at:v${at_version} ./docker"
       sh "rm -rf ../UT_AR_TestFramework"
       sh "docker push 192.168.84.23:5000/${BRANCH_NAME}/anyrobot-at:v${at_version}"
       sh "docker rmi 192.168.84.23:5000/${BRANCH_NAME}/anyrobot-at:v${at_version}"
    }
}

