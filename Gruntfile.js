module.exports = function (grunt) {
    'use strict';

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        clean: {
            dist: 'dist'
        },
        sass: {
            dist: {
                options: {
                    style: 'compressed',
                    loadPath: ['node_modules/bootstrap/scss/',
                               'scss/']
                },
                files: {
                    'assets/style.css': 'scss/mph.scss'
                }
            }
        }
    });
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.registerTask('default', ['sass']);
};
