/* gom-app-application.c
 *
 * Copyright 2022 Fernando Barbosa Ferreira Lopes
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include "config.h"

#include "gom-app-application.h"
#include "ui/app/gom-app-window.h"

struct _GomAppApplication
{
  AdwApplication parent_instance;
};

G_DEFINE_TYPE (GomAppApplication, gom_app_application, ADW_TYPE_APPLICATION)

GomAppApplication *
gom_app_application_new (const char        *application_id,
                         GApplicationFlags  flags)
{
  g_return_val_if_fail (application_id != NULL, NULL);

  return g_object_new (GOM_APP_TYPE_APPLICATION,
                       "application-id", application_id,
                       "flags", flags,
                       NULL);
}

static void
gom_app_application_activate (GApplication *app)
{
  GtkWindow *window;

  g_assert (GOM_APP_IS_APPLICATION (app));

  window = gtk_application_get_active_window (GTK_APPLICATION (app));
  if (window == NULL)
    window = g_object_new (GOM_APP_TYPE_WINDOW,
                           "application", app,
                           NULL);

  gtk_window_present (window);
}

static void
gom_app_application_class_init (GomAppApplicationClass *klass)
{
  GApplicationClass *app_class = G_APPLICATION_CLASS (klass);

  app_class->activate = gom_app_application_activate;
}

static void
gom_app_application_about_action (GSimpleAction *action,
                                  GVariant      *parameter,
                                  gpointer       user_data)
{
  static const char *developers[] = {"Fernando Barbosa Ferreira Lopes", NULL};
  GomAppApplication *self = user_data;
  GtkWindow *window = NULL;

  g_assert (GOM_APP_IS_APPLICATION (self));

  window = gtk_application_get_active_window (GTK_APPLICATION (self));

  adw_show_about_window (window,
                         "application-name", "gom-app",
                         "application-icon", "plasmus777.gnome.GpuOffloadingManager",
                         "developer-name", "Fernando B. F. Lopes",
                         "version", "0.1.0",
                         "developers", developers,
                         "copyright", "© 2022 Fernando Barbosa Ferreira Lopes",
                         NULL);
}

static void
gom_app_application_quit_action (GSimpleAction *action,
                                 GVariant      *parameter,
                                 gpointer       user_data)
{
  GomAppApplication *self = user_data;

  g_assert (GOM_APP_IS_APPLICATION (self));

  g_application_quit (G_APPLICATION (self));
}

static const GActionEntry app_actions[] = {
  { "quit", gom_app_application_quit_action },
  { "about", gom_app_application_about_action },
  { "shortcuts", gom_app_application_about_action },
  { "preferences", gom_app_application_about_action },
};

static void
gom_app_application_init (GomAppApplication *self)
{
  g_action_map_add_action_entries (G_ACTION_MAP (self),
                                   app_actions,
                                   G_N_ELEMENTS (app_actions),
                                   self);
  gtk_application_set_accels_for_action (GTK_APPLICATION (self),
                                         "app.quit",
                                         (const char *[]) { "<primary>q", NULL });
}

