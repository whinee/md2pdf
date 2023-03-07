<h1 align="center" style="font-weight: bold">
    Translations
</h1>


<div class="toc"><h2 id="toc"><b><a href="#toc">Table of Contents</a></b></h2>
<ul><li><a href="#summary">Summary</a></li><li><a href="#definition-of-terms">Definition of Terms</a></li><li><a href="#translation-directory">Translation Directory</a></li><li><a href="#notes-for-translators">Notes for Translators</a><ul><li><a href="#notes-for-translators-rule-of-thumb">Rule of Thumb</a></li><li><a href="#notes-for-translators-variables">Variables</a></li></ul></li><li><a href="#translation-file">Translation File</a><ul><li><a href="#translation-file-structure">Structure</a><ul><li><a href="#translation-file-structure-metadata">metadata</a><ul><li><a href="#translation-file-structure-metadata-version">version</a><ul><li><a href="#translation-file-structure-metadata-version-for-the-author">For The Author</a></li><li><a href="#translation-file-structure-metadata-version-for-the-translators">For The Translators</a></li></ul></li><li><a href="#translation-file-structure-metadata-contributors">contributors</a><ul><li><a href="#translation-file-structure-metadata-contributors-name">name</a></li><li><a href="#translation-file-structure-metadata-contributors-desc">desc</a></li><li><a href="#translation-file-structure-metadata-contributors-links">links</a><ul><li><a href="#translation-file-structure-metadata-contributors-links-anilist">anilist</a></li><li><a href="#translation-file-structure-metadata-contributors-links-discord">discord</a></li><li><a href="#translation-file-structure-metadata-contributors-links-email">email</a></li><li><a href="#translation-file-structure-metadata-contributors-links-github">github</a></li><li><a href="#translation-file-structure-metadata-contributors-links-reddit">reddit</a></li><li><a href="#translation-file-structure-metadata-contributors-links-twitter">twitter</a></li></ul></li></ul></li></ul></li><li><a href="#translation-file-structure-splash">splash</a><ul><li><a href="#translation-file-structure-splash-str">str</a></li><li><a href="#translation-file-structure-splash-desc">desc</a></li><li><a href="#translation-file-structure-splash-tln">tln</a></li></ul></li><li><a href="#translation-file-structure-text">text</a><ul><li><a href="#translation-file-structure-text-scope">{scope}</a><ul><li><a href="#translation-file-structure-text-scope-class">{class}</a><ul><li><a href="#translation-file-structure-text-scope-class-key">{key}</a><ul><li><a href="#translation-file-structure-text-scope-class-key-str">str</a></li><li><a href="#translation-file-structure-text-scope-class-key-desc">desc</a></li><li><a href="#translation-file-structure-text-scope-class-key-tln">tln</a></li></ul></li></ul></li></ul></li></ul></li></ul></li></ul></li></ul></div>

<h2 id="summary"><b><a href="#summary">Summary</a></b></h2>

While there are no future plans for expanding to the global audience, of which most does not speak English, this application is ready for internationalization.

<h2 id="definition-of-terms"><b><a href="#definition-of-terms">Definition of Terms</a></b></h2>

[i18n](https://en.wikipedia.org/wiki/Internationalization_and_localization#Naming) (abbreviation, [numeronym](https://en.wikipedia.org/wiki/Numeronym)): stands for internationalization; process of designing a software application so that it can be adapted to various languages and regions without engineering changes

<h2 id="translation-directory"><b><a href="#translation-directory">Translation Directory</a></b></h2>

The files that contain the translations can be located at `./dev/constants/version/{u}/{d}/lang/`

whereas:

- `{u}` refers to the `user` version that uses the constants under this directory
- `{d}` refers to the `dev` version that uses the constants under this directory

<details>
<summary>Notes:</summary>

For more information, visit the <a href="notes-to-self.md#versioning-system">notes for whi~nyaan!</a>.

</details>

<h2 id="notes-for-translators"><b><a href="#notes-for-translators">Notes for Translators</a></b></h2>

For those who want to translate this application, please read all of the following text.

<h2 id="notes-for-translators-rule-of-thumb"><b><i><a href="#notes-for-translators-rule-of-thumb">Rule of Thumb</a></i></b></h2>

This is written by the author with no consideration for other languages. And as such, recommendations and suggestions are highly appreciated.

- Any technical terminologies should be left untranslated, unless noted by the author (developer) otherwise.
- Any technical phrase that cannot be translated properly to the target language should be translated without oversimplifying; Oversimplification might lead to a misunderstanding
- Unless the tone affects the meaning of the text or unless stated otherwise, translators should not preserve the author's tone and should translate it with a neutral tone

<h2 id="notes-for-translators-variables"><b><i><a href="#notes-for-translators-variables">Variables</a></i></b></h2>

You might see a text that is enclosed in a bracket, like the following:

```txt
{version}
```

These are variables, and are replaced with information in the application before displaying them to the user.

So, our example would be displayed to the users as such:

```txt
69.4.20
```

As you can see, it is crucial for displaying information to the users.

When translating a piece of text, make sure to put these variables in an appropriate place, and do not translate its name.

As an example, we will translate this English text:

```txt
Thank you for using {app_name}!
```

To Tagalog:

<!--- cSpell:disable -->
```txt
Sa paggamit ng {app_name}, ako ay taos-pusong nagpapasalamat sa iyong pagtangkilik!
```
<!--- cSpell:enable -->

The variable's name is not translated.

In this next example, the variable is already in a fixed position:

```txt
{app_name} version: {version}
```

The Tagalog translation should look like this:

<!--- cSpell:disable -->
```txt
bersyon ng {app_name}: {version}
```
<!--- cSpell:enable -->

The `app_name` variable changed places to translate properly. However, there is no need for `version` to do so, as it is formatted.

<h2 id="translation-file"><b><a href="#translation-file">Translation File</a></b></h2>

A translation file can be found under the [translation directory](#translation-directory).

Whereas, its name is ISO 639-1 language code that corresponds to its contained translations.

<h2 id="translation-file-structure"><b><i><a href="#translation-file-structure">Structure</a></i></b></h2>

<h2 id="translation-file-structure-metadata"><a href="#translation-file-structure-metadata">metadata</a></h2>

Metadata of the translation.

<h2 id="translation-file-structure-metadata-version"><i><a href="#translation-file-structure-metadata-version">version</a></i></h2>

Version of the translation.

<h3 id="translation-file-structure-metadata-version-for-the-author"><b><a href="#translation-file-structure-metadata-version-for-the-author">For The Author</a></b></h3>

Given a version number `major`.`minor`.`patch`, bump the:

- `major` version when you make a significant change in the contents of a text or the description along side it, that you think it warrants a change in all of the translations.

- `minor` version when you make a change in the contents of a text or the description along side it, which does not warrant a change in all of the translations. Example are modifying text to use much more understandable words.

- `patch` version when you fix a typographical error in a text. This might induce a change in other translation, but does not warrant otherwise.

Changing the schema, or any key names shall warrant a `dev` version bump for the application. You break the english text for this application, you fix every other translation.

<h3 id="translation-file-structure-metadata-version-for-the-translators"><b><a href="#translation-file-structure-metadata-version-for-the-translators">For The Translators</a></b></h3>

As the app is written in English, follow the latest version of the english text.

The translation will be bumped as per the specification written [here](#translation-file-structure-metadata-version-for-the-author).

If you updated your translations to match that of the current English translation, change the version to the current version of the English translation.

<h2 id="translation-file-structure-metadata-contributors"><i><a href="#translation-file-structure-metadata-contributors">contributors</a></i></h2>

List of translation contributors' information, for attribution purposes.

<h3 id="translation-file-structure-metadata-contributors-name"><b><a href="#translation-file-structure-metadata-contributors-name">name</a></b></h3>

Name of the contributor.

It can be an alias, nickname, or a full name. As long as you are happy with being credited using that name, I have no problem with it.

Obscene and/or offensive names however will be apprehended. Otherwise, be creative.

<h3 id="translation-file-structure-metadata-contributors-desc"><b><a href="#translation-file-structure-metadata-contributors-desc">desc</a></b></h3>

Describe yourself.

If you're getting credited, go all out. You can even advertise your personal project. As long as the contents are not obscene or offensive, I'm fine with it.

<h3 id="translation-file-structure-metadata-contributors-links"><b><a href="#translation-file-structure-metadata-contributors-links">links</a></b></h3>

Dictionary of links to your contacts, social media, and whatnot.

<h3 id="translation-file-structure-metadata-contributors-links-anilist"><b><i><a href="#translation-file-structure-metadata-contributors-links-anilist">anilist</a></i></b></h3>

Anilist username.

Example:

```yaml
anilist: whinyaan
```

Links to https://anilist.co/user/whinyaan.

<h3 id="translation-file-structure-metadata-contributors-links-discord"><b><i><a href="#translation-file-structure-metadata-contributors-links-discord">discord</a></i></b></h3>

Key-value pairs of Discord tag and their snowflake.

Example:

```yaml
discord:
    whi_ne#4783:
        848092597822160907
```

Links to [whi_ne#4783](https://discord.com/users/848092597822160907).

<h3 id="translation-file-structure-metadata-contributors-links-email"><b><i><a href="#translation-file-structure-metadata-contributors-links-email">email</a></i></b></h3>

List of electronic mail addresses.

Example:

```yaml
email:
    - whinyaan@protonmail.com
```

Links to [whinyaan@protonmail.com](mailto:whinyaan@protonmail.com).

<h3 id="translation-file-structure-metadata-contributors-links-github"><b><i><a href="#translation-file-structure-metadata-contributors-links-github">github</a></i></b></h3>

Github username.

Example:

```yaml
github: whinee
```

Links to https://github.com/whinee.

<h3 id="translation-file-structure-metadata-contributors-links-reddit"><b><i><a href="#translation-file-structure-metadata-contributors-links-reddit">reddit</a></i></b></h3>

Reddit username.

Example:

```yaml
reddit: whi-nyaan
```

Links to https://reddit.com/user/whi-nyaan.

<h3 id="translation-file-structure-metadata-contributors-links-twitter"><b><i><a href="#translation-file-structure-metadata-contributors-links-twitter">twitter</a></i></b></h3>

Twitter username.

Example:

```yaml
twitter: whi_nyaan
```

Links to https://twitter.com/whi_nyaan.

<h2 id="translation-file-structure-splash"><a href="#translation-file-structure-splash">splash</a></h2>

Dictionary of random stuff to be displayed at startup of the application.

Example:

```yml
music_artist_rec:
    str: Listen to Kanro! https://kanromusic.com
    desc: Author's music artist recommendation
```

<h2 id="translation-file-structure-splash-str"><i><a href="#translation-file-structure-splash-str">str</a></i></h2>

The actual splash message.

<h2 id="translation-file-structure-splash-desc"><i><a href="#translation-file-structure-splash-desc">desc</a></i></h2>

Description of the splash message. Might be useful to keep the translation accurate at an acceptable margin. Will not be displayed.

<h2 id="translation-file-structure-splash-tln"><i><a href="#translation-file-structure-splash-tln">tln</a></i></h2>

Stands for translators' notes, used by translators to describe to the next translators any compromises done to translate the text to a certain language, or whatnot.

<h2 id="translation-file-structure-text"><a href="#translation-file-structure-text">text</a></h2>

Dictionary of scopes, classes, and keys (dictionary) of text to display in the application.

Example:

```yml
cli:
    init:
        choose_language:
            str: Choose language
            desc: |-
                Choose app language
```

<h2 id="translation-file-structure-text-scope"><i><a href="#translation-file-structure-text-scope">{scope}</a></i></h2>

There are three scopes allowed, but only the first two are applicable:

- common
- cli
- gui

The first scope is class of keys that can be used in both the CLI and GUI versions of the app. This includes the description and motto of the program, prompts like `yes` or `no`, and whatnot. The rest is self-explanatory.

<h3 id="translation-file-structure-text-scope-class"><b><a href="#translation-file-structure-text-scope-class">{class}</a></b></h3>

This is where keys are categorized. For example, keys that convey information regarding the application can be put under the `info` class, while the keys that are used for prompting the users can be put under the `prompt` class.

<h3 id="translation-file-structure-text-scope-class-key"><b><i><a href="#translation-file-structure-text-scope-class-key">{key}</a></i></b></h3>

This is the name of the key. There is no general naming convention, but the developer seems to have one in her mind.

<h3 id="translation-file-structure-text-scope-class-key-str"><a href="#translation-file-structure-text-scope-class-key-str">str</a></h3>

The string in the language defined by the language file.

<h3 id="translation-file-structure-text-scope-class-key-desc"><a href="#translation-file-structure-text-scope-class-key-desc">desc</a></h3>

Description of the key. Might be useful to keep the translation accurate at an acceptable margin. Will not be displayed.

<h3 id="translation-file-structure-text-scope-class-key-tln"><a href="#translation-file-structure-text-scope-class-key-tln">tln</a></h3>

Stands for translators' notes, used by translators to describe to the next translators any compromises done to translate the text to a certain language, or whatnot.
