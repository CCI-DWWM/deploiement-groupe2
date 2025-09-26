# Développement et mise à disposition d'application IoT avec dashboard

Vous voulez mettre en place les éléments permettant de suivre des mesures de capteur IoT sur le terrain

![MongoDB](https://img.shields.io/badge/-MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Algorithmique](https://img.shields.io/badge/-Algorithmique-blue?style=for-the-badge)
![Git](https://img.shields.io/badge/-Git-F05032?style=for-the-badge&logo=git&logoColor=white)

## Ressources

- [Render.com](https://render.com/docs/deploys)
- [Services Azure](https://azure.microsoft.com/fr-fr)
- Créer et déployer une application de machine virtuelle](https://learn.microsoft.com/fr-fr/azure/virtual-machines/vm-applications-how-to?tabs=TAR%2Ccli1%2Ccli2%2Crest3%2Crest4)
- [MongoDB](https://www.mongodb.com/)
- [Documentation Docker](https://docs.docker.com/)
- [protocole SMTP (email)](https://fr.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)
- [tuto "Progressive Web Apps (PWA)"](https://laconsole.dev/blog/guide-pwa)
- [Capteur VS133](https://www.milesight.com/iot/product/lorawan-sensor/vs133)

## Contexte du projet

Le client (CCI, VDLN, ville) veux avoir accès aux données des capteurs

## Modalités pédagogiques

Travail par groupe (3)

### Objectifs :

* mettre en place les éléments permettant de récupérer les mesures des capteurs
* déployer automatiquement
* inclure une application PWA (si déjà fait)
* utilisation de git avec des branches au sein d'un groupe
* envoi d'email d'alerte
* prendre en compte les capteurs MILESIGHT VS133

### Étapes :

1. projet github (reprise du précédent possible)
2. Inclure les sources python (MQTT, MongoDB, SMTP)
3. Configurer l'environnement (.env, à ne pas inclure dans github)
4. Tester la configuration
5. Création du Dockerfile et tester en local si possible
6. Déploiement sur Render ou Azure

## Modalités d'évaluation

Construction de services permettant d'extraire les données, et de les afficher

## Livrables
- Lien GitHub
- URL application sur le cloud

## Critères de performance
- Application fonctionnelle et accessible sur internet
- Données stockées dans Mongo
- Appli PWA disponible
