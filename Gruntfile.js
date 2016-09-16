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
        },
        copy: {
            main: {
                files: [
                    {src: 'node_modules/bootstrap/dist/js/bootstrap.min.js',
                     dest: 'assets/bootstrap.min.js'},
                    {src: 'node_modules/jquery/dist/jquery.min.js',
                     dest: 'assets/jquery.min.js'}
                ]
            },
            pygments: {
                src: 'node_modules/pygments-css/default.css',
                dest: 'assets/pygments.css',
                options: {
                    process: function (content, srcpath) {
                        return content.replace(/codehilite/g, 'highlight');
                    }
                }
            }
        }
    });
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.registerTask('default', ['sass', 'copy']);
};
