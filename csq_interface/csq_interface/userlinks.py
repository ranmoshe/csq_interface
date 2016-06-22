class UserLinks():
    '''
    Returns the appropriate links for the user,
    and their states (done / next / disabled)
    '''

    def __init__(self, user):
        self.user = user

    def get_links(self):
        links = [
                ('/upload/', 'Upload Data and Config Files', 'done'),
                ('/manual_config/', 'Configure Manually (optional)', 'next'),
                ('/graph/', 'Display Causal Graph', 'disabled'),
                ]
        return links
