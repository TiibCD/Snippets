// Utilisation de l'API Regex de Java

// Chaine test
String vTexte = "Texte à formatter";

// On définir la regex
String vRegex = ^(.+)( Example | Example )(.+)

// On définit le pattern avec la regex
Pattern vPattern = Pattern.compile(vRegex);            
       
// Si un pattern est définit on l'applique
 if (vPattern != null)
{
      Matcher vMatcher = vPattern.matcher(vTexte);
      if (vMatcher.find()
           && vMatcher.groupCount() >= 3)
      {
          vRetour += vMatcher.group(3);
      }
}
https://regex101.com/r/1KbAqR/1
