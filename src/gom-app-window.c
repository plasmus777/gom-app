/* gom-app-window.c
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

#include "gom-app-window.h"

struct _GomAppWindow
{
  AdwApplicationWindow  parent_instance;

  /* Template widgets */
  GtkHeaderBar        *header_bar;
  GtkLabel            *label;
};

G_DEFINE_FINAL_TYPE (GomAppWindow, gom_app_window, ADW_TYPE_APPLICATION_WINDOW)

static void
gom_app_window_class_init (GomAppWindowClass *klass)
{
  GtkWidgetClass *widget_class = GTK_WIDGET_CLASS (klass);

  gtk_widget_class_set_template_from_resource (widget_class, "/plasmus777/gnome/GpuOffloadingManager/gom-app-window.ui");
  gtk_widget_class_bind_template_child (widget_class, GomAppWindow, header_bar);
  gtk_widget_class_bind_template_child (widget_class, GomAppWindow, label);
}

static void
gom_app_window_init (GomAppWindow *self)
{
  gtk_widget_init_template (GTK_WIDGET (self));
}
