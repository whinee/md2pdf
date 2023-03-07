# **[src](index.md).[info](info.md)**

    

    
<h2><b><a href="#var" id="var">Variables</a></b></h2>

    
`CHOLDER`
HTML text of copyright holders of this project

    
`PROJECT_NAME`
Project's name

    
`SVER`
The current version of the project, compliant with the semver.

This project uses a modified semver. For more information, visit [this link](../../../notes-to-self.md#versioning-system).

    
`VARIANT`
The application variant

This is useful for debugging, and for initializing the application's configuration.
Following are the allowed variants:

- `installable`: for when the application is packed as an installable application
- `package`: for when the application is published on PyPi (as a Python Library)
- `portable`: for when the application is packed as a portable application

    
`VLS`
The current version of the project as a list.

The list consists of 6 integers, which represent the following:
    - User
    - Dev
    - Minor
    - Patch
    - Prerelease Identifier
        The prerelease identifier number corresponds to the following values:
            0: alpha
            1: beta
            2: release candidate or rc
            3: none
    - Prerelease Version