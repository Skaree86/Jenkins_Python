def cause = currentBuild.getBuildCauses('hudson.model.Cause$UserIdCause')
            def PLAT_FAVORIS = null

stage('Get username') {
    //steps {
    echo "Bonjour ${cause.userName}!"
    //}
}
stage('Get input') {
    PLAT_FAVORIS = input (
                       message: "Quel est ton plat favoris ${cause.userName}?",
                       ok: "Valider",
                       parameters: [string(defaultValue: "huile",
                                           name: "PLAT_FAVORIS",
                                           trim: true)]
                   )
}
stage('Get answer') {
    echo "${PLAT_FAVORIS} , vraiment?!"
}
stage('Send Python') {
    echo "toujours pas"
    sh 'ls'
}
