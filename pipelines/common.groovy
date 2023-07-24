// Helper Functions
def getCauseUserId() {
    def userIdCause = currentBuild.getBuildCauses('hudson.model.Cause$UserIdCause');
    final String nameFromUserIdCause = userIdCause != null && userIdCause[0] != null ? userIdCause[0].userId : null;
    if (nameFromUserIdCause != null) {
        return nameFromUserIdCause + "@idir";
    } else {
        return 'unknown'
    }
}

return this
