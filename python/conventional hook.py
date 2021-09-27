#!/usr/bin/env python3
# Original source: https://www.cerenit.fr/blog/git-conventional-commits/

import re, sys, os

convention = """https://www.conventionalcommits.org

Structure   : type(scope)! : message
Exemple     : feat(lang) : ajout trad anglaise

- Types   [Obligatoire]     : build | chore | ci | docs | feat | fix | perf | refactor | revert | style | test | BREAKING CHANGE
- Scope   [Non obligatoire] : permet de préciser le périmètre du commit
- !       [Non obligatoire] : permet d'attirer l'attention sur un breaking change
- Message [Obligatoire]     : permet de décrire ce qui a été fait et pourquoi mais pas comment sinon utilisation du body
"""

def main():
    # On définit la regex 
    regex = r'(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test|BREAKING CHANGE)(\([\w\-\s]+\))?!?\s?:\s.*'
    # On récupère les arguments passés en paramètres
    commitMessage = sys.argv[1]
    # Si on ne trouve pas de correspondance avec la regex alors on n'a pas respecté la convention
    if re.match(regex, commitMessage) is None:
        print("\n>> PRE COMMIT CHECK FAILED!")
        print("\nVotre commit ne respecte pas la convention :")
        print(convention)
        sys.exit(1)
    else:
        print("\n>> PRE COMMIT CHECK PASSED!")

if __name__ == "__main__":
    main()